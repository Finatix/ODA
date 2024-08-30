"""service for the ConversationManager
"""

from ..components.api import SessionData
from ..components.conversation import ConversationManager, SessionConversationManager
from .session_data import session_data
from fastapi import Depends
from typing import Annotated


def conversation_manager(session_data: Annotated[SessionData, Depends(session_data)]) -> ConversationManager:
    """creates the ConversationManager service

    Currently it's the SessionConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return SessionConversationManager(session_data)
