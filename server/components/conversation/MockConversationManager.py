"""
mock implementation of ConversationManager
"""

from ..models import Conversation, PastConversation
from .ConversationManager import ConversationManager
from typing import override
from uuid import UUID

class MockConversationManager(ConversationManager):
    """
    mock implementation of ConversationManager
    """

    def __init__(self):
        self.__conversations: dict[UUID, Conversation] = {}

    @override
    def get_conversation(self, token: UUID) -> Conversation:
        if token not in self.__conversations:
            conversation = Conversation(token=token)
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
