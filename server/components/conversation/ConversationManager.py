"""Declares an interface for managing conversations
"""

from ..api import PastConversation
from ..exceptions import conversationTokenNotFound
from abc import ABC, abstractmethod
from uuid import UUID, uuid4

class ConversationManager(ABC):
    """
    interface for managing conversation
    """

    @abstractmethod
    def get_past_conversation(self, token: UUID) -> PastConversation:
        """finds a past conversation by its token

        Args:
            token (UUID): token of the conversation

        Raise:
            ConversationNotFoundException if toke is not found

        Returns:
            PastConversation: the found conversion
        """
        conversationTokenNotFound(token)

    @abstractmethod
    def start_conversation(self) -> UUID:
        """
        Starts a new conversation

        Returns:
            UUID: the token of the conversation
        """
        return uuid4()
