from pydantic import BaseModel
from typing import Annotated

class Message(BaseModel):
    id: Annotated[str, "the UUID of the message"]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[str, "the timestamp"]
    conversation: Annotated[str, "the UUID token of the conversation"]
