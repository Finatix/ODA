"""model for data stored in session
"""

from . import Conversation
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID

class SessionData(BaseModel):
    conversations: Annotated[dict[UUID, Conversation], "the conversations of this session", Field(default={})]
