from pydantic import BaseModel
from typing import Annotated
from uuid import UUID

class PastConversation(BaseModel):
    title: Annotated[str, "some kind of title"]
    id: Annotated[UUID, "the conversation token"]
