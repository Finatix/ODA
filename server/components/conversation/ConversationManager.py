from abc import ABC, abstractmethod
from typing import override
from uuid import UUID, uuid4

class ConversationManager(ABC):
    """
    interface class for managing conversation
    """
    @abstractmethod
    def start_conversation(self) -> UUID:
        """
        Starts a new conversation

        Returns:
            UUID: the token of the conversation
        """
        return uuid4()
