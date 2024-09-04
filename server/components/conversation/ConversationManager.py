"""Declares an interface for managing conversations
"""

from ..models import Conversation, PastConversation
from ..exceptions import conversationTokenNotFound
from abc import ABC, abstractmethod
from uuid import UUID, uuid4

class ConversationManager(ABC):
    """
    interface for managing conversation
    """

    @abstractmethod
    def get_conversation(self, token: UUID) -> Conversation:
        """finds a conversation by its token

        Args:
            token (UUID): token of the conversation

        Raise:
            ConversationNotFoundException if token is not found

        Returns:
            Conversation: the found conversion
        """
        conversationTokenNotFound(token)

    @abstractmethod
    def get_past_conversation(self, token: UUID) -> PastConversation:
        """finds a past conversation by its token

        Args:
            token (UUID): token of the conversation

        Raise:
            ConversationNotFoundException if token is not found

        Returns:
            PastConversation: the found conversion
        """
        conversation = self.get_conversation(token)

        return conversation.to_past_conversation()

    @abstractmethod
    def save_conversation(conversation: Conversation) -> None:
        """saves the given conversation

        Args:
            conversation (Conversation): the conversation to be saved
        """
        pass

    @abstractmethod
    def start_conversation(self) -> Conversation:
        """
        Starts a new conversation

        Returns:
            UUID: the token of the conversation
        """
        conversation = Conversation()

        self.save_conversation(conversation)

        return conversation
