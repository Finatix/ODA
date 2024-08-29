from pydantic import BaseModel
from typing import Annotated

class ConversationResponse(BaseModel):
    conversationToken: Annotated[str, "the UUID token of the conversation"]
    response: Annotated[str, "some kind of response"]
