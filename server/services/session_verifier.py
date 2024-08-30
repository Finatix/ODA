"""service definition for session verifier
"""

from ..components.session import SessionVerifier

def session_verifier() -> SessionVerifier:
    return SessionVerifier()
