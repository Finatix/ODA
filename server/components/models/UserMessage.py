from pydantic import BaseModel
from typing import Annotated

class UserMessage(BaseModel):
    message: Annotated[str, "the message to be sent"]
