"""entrypoint of the python web app using FastAPI
"""

from .components.api import Conversation, ConversationResponse, PastConversation, UserMessage
from .services import conversation_manager, generator, ConversationManager, Generator
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Annotated
from uuid import UUID

# settings

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "resources" / "static"
HTML_DIR = STATIC_DIR / "html"

# webserver

app = FastAPI()

## static files
app.mount("/static", StaticFiles(directory=STATIC_DIR))

## frontend
@app.head("/")
@app.get("/", summary="Returns the frontend", response_class=HTMLResponse)
async def index():
    path = HTML_DIR / "index.html"

    return path.read_text()

## api

@app.post("/api/conversations", summary="Start a conversation")
def start_conversation(conversation_manager: Annotated[ConversationManager, Depends(conversation_manager)]) -> ConversationResponse:
    """Start a conversation"""

    token = conversation_manager.start_conversation()

    return ConversationResponse(conversationToken=token)

@app.get("/api/conversations", summary="Get conversations by tokens")
def get_conversations(
        conversation_manager: Annotated[ConversationManager, Depends(conversation_manager)],
        tokens: Annotated[list[UUID], "List of conversation tokens"]
    ) -> list[PastConversation]:
    """Get conversations by tokens

    Args:
        tokens (list[UUID]): List of conversation tokens

    Returns:
        list[PastConversation]: List of conversations
    """
    conversations = []
    for token in tokens:
        conversation = conversation_manager.get_past_conversation(token)
        conversations.append(conversation)

    return conversations

@app.post("/api/conversations/{conversation_token}/messages", summary="Send a message in a conversation")
def send_message(
        conversation_manager: Annotated[ConversationManager, Depends(conversation_manager)],
        conversation_token: Annotated[str, "Token of the conversation"],
        generator: Annotated[Generator, Depends(generator)],
        message: Annotated[UserMessage, "the message"]) -> ConversationResponse:

    conversation = conversation_manager.get_conversation(conversation_token)

    prompt = message.message

    conversation.add_message(message=prompt, sender="User")

    response = generator.generate(prompt, conversation)

    conversation.add_message(message=response, sender="AI")

    return ConversationResponse(conversationToken=conversation_token, response=response)

@app.get("/api/conversations/{conversation_token}", summary="Get conversation details by token")
def get_conversation_details(
        conversation_manager: Annotated[ConversationManager, Depends(conversation_manager)],
        conversation_token: Annotated[str, "Token of the conversation session"]
    ) -> Conversation:

    return conversation_manager.get_conversation(conversation_token)
