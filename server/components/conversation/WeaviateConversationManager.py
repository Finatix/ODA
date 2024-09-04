"""
implementation of ConversationManager with a Weaviate database
"""

from ..models import Conversation, Message, PastConversation
from ..exceptions import conversationTokenNotFound, ConversationException
from .ConversationManager import ConversationManager
from datetime import datetime, timedelta, UTC
from logging import getLogger, Logger
from typing import override
from uuid import UUID
from weaviate import WeaviateClient
from weaviate.classes.config import Configure, DataType, Property
from weaviate.classes.query import Filter, Sort
from weaviate.collections.collection.sync import Collection

class WeaviateConversationManager(ConversationManager):
    """
    implementation of ConversationManager with a Weaviate database
    """

    SCHEMA_NAME: str = "Conversation"

    def __init__(self, client: WeaviateClient):
        self.__client: WeaviateClient = client
        self.__cache: dict[UUID, Conversation] = {}
        self.__logger: Logger = getLogger(__name__)

    def __del__(self):
        self.__delete_old_conversations()
        self.__close()

    def __enter__(self):
        self.__connect()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close()

    @override
    def get_conversation(self, token: UUID) -> Conversation:
        if token not in self.__cache:
            return self.__read(token)

        return self.__cache[token]

    @override
    def get_past_conversation(self, token: UUID) -> PastConversation | None:
        return super().get_past_conversation(token)

    @override
    def save_conversation(self, conversation: Conversation) -> None:
        self.__write(conversation)

    @override
    def start_conversation(self) -> Conversation:
        return super().start_conversation()

    @property
    def __is_connected(self) -> bool:
        return self.__client.is_connected()

    def __connect(self) -> None:
        if not self.__is_connected:
            self.__client.connect()
            self.__logger.info("connected to weaviate")

    def __close(self) -> None:
        if self.__is_connected:
            self.__client.close()
            self.__logger.info("connection to weaviate closed")

    def __reconnect(self) -> None:
        self.__close()
        self.__connect()

    def __delete_old_conversations(self) -> None:
        if not self.__is_connected:
            return
        collection = self.__get_collection()
        if collection is None:
            return
        yesterday = datetime.now(UTC) - timedelta(days=1)
        response = collection.query.fetch_objects(
            filters=Filter.by_update_time().less_than(yesterday),
            sort=Sort.by_update_time()
        )
        for o in response.objects:
            collection.data.delete_by_id(o.uuid)
            self.__cache.pop(o.uuid, None)
            self.__logger.info(f"deleted old conversation {o.uuid}")

    def __read(self, token: UUID, reconnected: bool = False) -> Conversation | None:
        self.__logger.debug(f"read conversation {token}")
        collection = self.__get_collection()
        if collection is None:
            conversationTokenNotFound(token)
        if not collection.data.exists(token):
            conversationTokenNotFound(token)

        data_object = collection.query.fetch_object_by_id(token)

        if data_object is None:
            if reconnected:
                raise ConversationException("data and query are not in sync, even after reconnect")
            self.__logger.error("data and query are not in sync, reconnect ...")
            self.__reconnect()
            return self.__read(token, True)

        token = data_object.uuid
        properties = data_object.properties
        properties["token"] = token

        metadata = data_object.metadata
        timestamp = metadata.creation_time if metadata.last_update_time is None else metadata.last_update_time
        properties["timestamp"] = timestamp

        conversation = Conversation.model_validate(properties)

        self.__cache[token] = conversation

        self.__logger.debug(f"loaded conversation {conversation.model_dump_json(indent=4)}")

        return conversation

    def __write(self, conversation: Conversation) -> None:
        collection = self.__get_collection(create=True)
        data = conversation.model_dump()
        if collection.data.exists(conversation.token):
            collection.data.update(uuid=conversation.token, properties=data)
            self.__logger.debug(f"update conversation {conversation.token}")
            return
        uuid = collection.data.insert(data)
        self.__logger.debug(f"inserted new conversation {uuid}")
        conversation.token = uuid
        for message in conversation.messages:
            message.conversation = uuid

        self.__write(conversation)
        self.__read(conversation.token)

    def __get_collection(self, create: bool = False) -> Collection | None:
        self.__connect()
        name = self.SCHEMA_NAME
        collections = self.__client.collections
        if not collections.exists(name):
            if create:
                return self.__create_collection()
            return
        return collections.get(name)

    def __create_collection(self) -> Collection:
        self.__logger.info("create collection for conversations")
        return self.__client.collections.create(
            self.SCHEMA_NAME,
            properties=[
                Property(name="title", data_type=DataType.TEXT),
                Property(name="messages", data_type=DataType.OBJECT_ARRAY, nested_properties=[
                    Property(name="message_id", data_type=DataType.UUID),
                    Property(name="text", data_type=DataType.TEXT),
                    Property(name="sender", data_type=DataType.TEXT),
                    Property(name="timestamp", data_type=DataType.DATE)
                ])
            ],
            inverted_index_config=Configure.inverted_index(index_timestamps=True)
        )
