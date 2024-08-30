"""service for session data
"""

from ..components.session import SessionData

def session_data() -> SessionData:
    return SessionData()
