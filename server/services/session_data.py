"""service for session data
"""

from ..components.session import SessionData
from .session_verifier import session_verifier
from fastapi import Depends
from typing import Annotated

def session_data(session_data: Annotated[SessionData, Depends(session_verifier)]) -> SessionData:
    return session_data
