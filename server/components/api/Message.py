from datetime import datetime, UTC
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

def timestamp() -> datetime:
    return datetime.now(UTC)

class Message(BaseModel):
    id: Annotated[UUID, "the UUID of the message", Field(default_factory=uuid4, alias="message_id")]
    text: Annotated[str, "the message text"]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[datetime, "the timestamp", Field(default_factory=timestamp)]
    conversation: Annotated[UUID, "the token of the conversation"]
