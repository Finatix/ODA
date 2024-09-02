"""service for the ConversationManager
"""

from ..components.conversation import ConversationManager, MockConversationManager


def conversation_manager() -> ConversationManager:
    """creates the ConversationManager service

    Currently it's just the MockConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return MockConversationManager()
