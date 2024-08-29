from .Message import Message
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

class Conversation(BaseModel):
    token: Annotated[UUID, "the token of the conversation", Field(default_factory=uuid4)]
    messages: Annotated[list[Message], "the message list", Field(default=[])]
