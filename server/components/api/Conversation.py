from .Message import Message
from .PastConversation import PastConversation
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

class Conversation(BaseModel):
    token: Annotated[UUID, "the token of the conversation", Field(default_factory=uuid4)]
    title: Annotated[str, "the optional title of the conversation", Field(default="")]
    messages: Annotated[list[Message], "the message list", Field(default=[])]

    def toPastConversation(self) -> PastConversation:
        return PastConversation(title=self.title, id=self.token)
