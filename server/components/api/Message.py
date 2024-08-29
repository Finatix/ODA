from pydantic import BaseModel
from typing import Annotated
from uuid import UUID

class Message(BaseModel):
    id: Annotated[UUID, "the UUID of the message"]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[str, "the timestamp"]
    conversation: Annotated[UUID, "the token of the conversation"]
