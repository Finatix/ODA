from .ConversationManager import ConversationManager
from typing import override
from uuid import UUID, uuid4

class MockConversationManager(ConversationManager):
    """
    mock implementation of ConversationManager
    """

    @override
    def start_conversation(self) -> UUID:
        """
        Starts a new conversation

        Returns:
            str: the UUID token of the conversation
        """
        return uuid4()
