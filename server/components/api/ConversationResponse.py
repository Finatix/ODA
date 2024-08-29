from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID

class ConversationResponse(BaseModel):
    conversationToken: Annotated[UUID, "the UUID token of the conversation"]
    response: Annotated[str, "some kind of response", Field(default="")]
