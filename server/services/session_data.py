"""service for session data
"""

from ..components.api import SessionData

def session_data() -> SessionData:
    return SessionData()
