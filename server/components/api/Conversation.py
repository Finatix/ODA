from .Message import Message
from pydantic import BaseModel
from typing import Annotated
from uuid import UUID

class Conversation(BaseModel):
    token: Annotated[UUID, "the token of the conversation"]
    messages: Annotated[list[Message], "the message list"]
