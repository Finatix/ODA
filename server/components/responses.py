from pydantic import BaseModel
from typing import Annotated

class Message(BaseModel):
    id: Annotated[str, "the UUID of the message"]
    sender: Annotated[str, "the message sender"]
    timestamp: Annotated[str, "the timestamp"]
    conversation: Annotated[str, "the UUID token of the conversation"]

class Conversation(BaseModel):
    token: Annotated[str, "the UUID token of the conversation"]
    messages: Annotated[list[Message], "the message list"]

class ConversationResponse(BaseModel):
    conversationToken: Annotated[str, "the UUID token of the conversation"]
    response: Annotated[str, "some kind of response"]

class PastConversation(BaseModel):
    title: Annotated[str, "some kind of title"]
    id: Annotated[str, "an UUID"]

class UserMessage(BaseModel):
    message: Annotated[str, "the message to be sent"]
