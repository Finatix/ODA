from .SessionData import SessionData
from fastapi_sessions.backends import SessionBackend
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier as __SessionVerifier
from fastapi import HTTPException
from typing import override
from uuid import UUID

class SessionVerifier(__SessionVerifier[UUID, SessionData]):
    def __init__(self):
        self.__backend: SessionBackend[UUID, SessionData] = None

    @override
    @property
    def identifier(self) -> str:
        return "session_verifier"

    @override
    @property
    def backend(self) -> SessionBackend[UUID, SessionData]:
        if self.__backend is None:
            self.__backend = InMemoryBackend[UUID, SessionData]()
        return self.__backend

    @override
    @property
    def auto_error(self) -> bool:
        return True

    @override
    @property
    def auth_http_exception(self) -> HTTPException:
        return HTTPException(status_code=403, detail="invalid session")

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True
