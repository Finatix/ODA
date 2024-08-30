"""service definitions for FastAPI dependeny injection
"""

from .components.ai import Generator, MockGenerator
from .components.api import SessionData
from .components.conversation import ConversationManager, SessionConversationManager
from fastapi import Depends
from typing import Annotated

def session_data() -> SessionData:
    """service for the session data

    Returns:
        SessionData: the service to be injected
    """
    return SessionData()

def conversation_manager(session_data: Annotated[SessionData, Depends(session_data)]) -> ConversationManager:
    """creates the ConversationManager service

    Currently it's the SessionConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return SessionConversationManager()

def generator() -> Generator:
    """creates the Generator service

    For starters its just the MockGenerator

    Returns:
        Generator: the service to be injected
    """
    return MockGenerator()
