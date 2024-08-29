from pydantic import BaseModel
from typing import Annotated

class PastConversation(BaseModel):
    title: Annotated[str, "some kind of title"]
    id: Annotated[str, "an UUID"]
