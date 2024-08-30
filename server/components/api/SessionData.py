"""model for data stored in session
"""

from . import Conversation
from pydantic import BaseModel, Field
from typing import Annotated

class SessionData(BaseModel):
    conversations: Annotated[list[Conversation], "the conversations of this session", Field(default=[])]
