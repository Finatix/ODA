"""exceptions raised by the application
"""

from typing import NoReturn
from uuid import UUID

class ODAException(Exception):
    pass

class ConversationException(ODAException):
    pass

class ConversationNotFoundException(ConversationException, LookupError):
        pass

def conversationTokenNotFound(token: UUID) -> NoReturn:
    raise ConversationNotFoundException(f"conversation token not found: {token}")
