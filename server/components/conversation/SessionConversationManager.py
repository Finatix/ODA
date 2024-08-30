"""
stores its converstions in the session
"""

from ..api import Conversation, PastConversation, SessionData
from ..exceptions import conversationTokenNotFound
from .ConversationManager import ConversationManager
from typing import override
from uuid import UUID

class SessionConversationManager(ConversationManager):
    """
    stores it conversations in the session data
    """

    def __init__(self, session_data: SessionData):
        self.__conversations: dict[UUID, Conversation] = session_data.conversations

    @override
    def get_conversation(self, token: UUID) -> Conversation:
        if token not in self.__conversations:
            conversationTokenNotFound(token)

        return self.__conversations[token]

    @override
    def get_past_conversation(self, token: UUID) -> PastConversation | None:

        conversation = self.get_conversation(token)

        return conversation.to_past_conversation()

    @override
    def start_conversation(self) -> UUID:
        uuid = super().start_conversation()
        self.__conversations[uuid] = Conversation(token=uuid)

        return uuid
