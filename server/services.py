"""service definitions for FastAPI dependeny injection
"""

from .components.conversation import ConversationManager, MockConversationManager

def conversation_manager() -> ConversationManager:
    """creates the ConversationManager service

    For starter. it's just the MockConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return MockConversationManager()
