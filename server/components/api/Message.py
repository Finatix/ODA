from datetime import datetime
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

def get_current_timestamp() -> str:
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class Message(BaseModel):
    id: Annotated[UUID, "the UUID of the message", Field(default_factory=uuid4)]
    text: Annotated[str, "the message text"]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[str, "the timestamp", Field(default_factory=get_current_timestamp)]
    conversation: Annotated[UUID, "the token of the conversation"]
