from .Message import Message
from pydantic import BaseModel
from typing import Annotated

class Conversation(BaseModel):
    token: Annotated[str, "the UUID token of the conversation"]
    messages: Annotated[list[Message], "the message list"]
