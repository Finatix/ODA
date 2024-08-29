from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

class PastConversation(BaseModel):
    title: Annotated[str, "some kind of title", Field(default="")]
    id: Annotated[UUID, "the conversation token", Field(default_factory=uuid4)]
