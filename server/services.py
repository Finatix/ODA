"""service definitions for FastAPI dependeny injection
"""

from .components.ai import Generator, MockGenerator
from .components.conversation import ConversationManager, MockConversationManager

def conversation_manager() -> ConversationManager:
    """creates the ConversationManager service

    For starters it's just the MockConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return MockConversationManager()

def generator() -> Generator:
    """creates the Generator service

    For starters its just the MockGenerator

    Returns:
        Generator: the service to be injected
    """
    return MockGenerator()
