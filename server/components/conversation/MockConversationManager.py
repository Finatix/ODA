"""
mock implementation of ConversationManager
"""

from ..api import Conversation, PastConversation
from .ConversationManager import ConversationManager, UUID
from typing import override

class MockConversationManager(ConversationManager):
    """
    mock implementation of ConversationManager
    """

    def __init__(self):
        self.__conversations: dict[UUID, Conversation] = {}

    @override
    def get_conversation(self, token: UUID) -> Conversation:
        if token not in self.__conversations:
            conversation = Conversation(token=token, title=f"Conversation {len(self.__conversations) + 1}")
            self.__conversations[token] = conversation

        return self.__conversations[token]

    @override
    def get_past_conversation(self, token: UUID) -> PastConversation | None:

        conversation = self.get_conversation(token)

        return conversation.to_past_conversation()

    @override
    def start_conversation(self) -> UUID:
        return super().start_conversation()
