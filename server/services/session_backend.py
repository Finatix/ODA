"""service for session backend
"""

from ..components.api import SessionData
from fastapi_sessions.backends import SessionBackend
from fastapi_sessions.backends.implementations import InMemoryBackend
from uuid import UUID

def session_backend() -> SessionBackend[UUID, SessionData]:
    return InMemoryBackend[UUID, SessionData]()
