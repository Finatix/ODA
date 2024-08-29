from .ConversationManager import ConversationManager, UUID
from typing import override

class MockConversationManager(ConversationManager):
    """
    mock implementation of ConversationManager
    """

    @override
    def start_conversation(self) -> UUID:
        """
        Starts a new conversation

        Returns:
            UUID: the UUID token of the conversation
        """
        return super().start_conversation()
