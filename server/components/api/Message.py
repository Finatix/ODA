from datetime import datetime
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

class Message(BaseModel):
    id: Annotated[UUID, "the UUID of the message", Field(default_factory=uuid4)]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[str, "the timestamp", Field(default_factory=datetime.now)]
    conversation: Annotated[UUID, "the token of the conversation"]
