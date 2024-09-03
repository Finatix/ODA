"""
implementation of ConversationManager with a Weaviate database
"""

from ..api import Conversation, Message, PastConversation
from ..exceptions import conversationTokenNotFound
from .ConversationManager import ConversationManager
from datetime import datetime, timedelta, UTC
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

    def __connect(self) -> None:
        if not self.__client.is_connected():
            self.__client.connect()

    def __close(self) -> None:
        if self.__client.is_connected():
            self.__client.close()

    def __delete_old_conversations(self) -> None:
        conversations = self.__get_conversations()
        if conversations is None:
            return
        yesterday = datetime.now(UTC) - timedelta(days=1)
        response = conversations.query.fetch_objects(
            filters=Filter.by_update_time().less_than(yesterday),
            sort=Sort.by_update_time()
        )
        for o in response.objects:
            conversations.data.delete_by_id(o.uuid)
            self.__cache.pop(o.uuid, None)

    def __read(self, token: UUID) -> Conversation | None:
        conversations = self.__get_conversations()
        if conversations is None:
            conversationTokenNotFound(token)
        if not conversations.data.exists(token):
            conversationTokenNotFound(token)

        data_object = conversations.query.fetch_object_by_id(token)

        if data_object is None:
            conversationTokenNotFound(token)

        token = data_object.uuid
        properties = data_object.properties
        properties["token"] = token

        metadata = data_object.metadata
        timestamp = metadata.creation_time if metadata.last_update_time is None else metadata.last_update_time
        properties["timestamp"] = timestamp

        conversation = Conversation(properties)

        self.__cache[token] = conversation

        print("fetched conversation: ", conversation)

        return conversation

    def __write(self, conversation: Conversation) -> None:
        conversations = self.__get_conversations(create=True)
        data = conversation.model_dump()
        if conversations.data.exists(conversation.token):
            conversations.data.update(uuid=conversation.token, properties=data)
        else:
            uuid = conversations.data.insert(data)
            conversation.token = uuid
            for message in conversation.messages:
                message.conversation = uuid
        self.__read(conversation.token)

    def __get_conversations(self, create: bool = False) -> Collection | None:
        self.__connect()
        name = self.SCHEMA_NAME
        collections = self.__client.collections
        if not collections.exists(name):
            if create:
                return self.__create_schema()
            return
        return collections.get(name)

    def __create_schema(self) -> Collection:
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
