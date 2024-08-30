"""exceptions raised by the application
"""

from typing import NoReturn
from uuid import UUID

class ODAException(Exception):
    pass

class ConversationEception(ODAException):
    pass

class ConversationNotFoundException(ConversationEception, LookupError):
        pass

def conversationTokenNotFound(token: UUID) -> NoReturn:
    raise ConversationNotFoundException(f"conversation token not found: {token}")
