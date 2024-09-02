"""
implementation of ConversationManager with a Weaviate database
"""

from ..api import Conversation, PastConversation
from .ConversationManager import ConversationManager
from typing import override
from uuid import UUID
from weaviate import WeaviateClient

class WeaviateConversationManager(ConversationManager):
    """
    implementation of ConversationManager with a Weaviate database
    """

    def __init__(self, client: WeaviateClient):
        self.__client: WeaviateClient = client
        self.__conversations: dict[UUID, Conversation] = {}

    @override
    def get_conversation(self, token: UUID) -> Conversation:
        if token not in self.__conversations:
            conversation = self.read(token)
            self.__conversations[token] = conversation

        return self.__conversations[token]

    @override
    def get_past_conversation(self, token: UUID) -> PastConversation | None:
        return super().get_past_conversation(token)

    @override
    def save_conversation(self, conversation: Conversation) -> None:
        self.__conversations[conversation.token] = conversation

    @override
    def start_conversation(self) -> Conversation:
        return super().start_conversation()

    def read(self, token: UUID) -> Conversation | None:
        return

    def write(self, conversation: Conversation) -> None:
        return

    def init(self) -> None:
        return
