from typing import override
from uuid import UUID

class ConversationManager:
    """
    interface class for managing conversation
    """

    def start_conversation(self) -> UUID:
        """
        Starts a new conversation

        Returns:
            UUID: the token of the conversation
        """
        raise NotImplementedError("abstract method call")
