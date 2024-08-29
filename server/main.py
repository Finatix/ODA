from .components.api import Conversation, ConversationResponse, PastConversation, UserMessage
from .services import conversation_manager, ConversationManager
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Annotated

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
    token = conversation_manager.start_conversation()

    return ConversationResponse(conversationToken=token)

@app.get("/api/conversations", summary="Get conversations by tokens")
def get_conversations(tokens: Annotated[list[str], "List of conversation tokens"]) -> list[PastConversation]:
    raise HTTPException(501, "not (yet) implemented")

@app.post("/api/conversations/{conversation_token}/messages", summary="Send a message in a conversation")
def send_message(
        coversation_token: Annotated[str, "Token of the conversation"],
        message: Annotated[UserMessage, "the message"]) -> ConversationResponse:
    raise HTTPException(501, "not (yet) implemented")

@app.get("/api/conversations/{conversation_token}", summary="Get conversation details by token")
def get_conversation_details(conversation_token: Annotated[str, "Token of the conversation session"]) -> Conversation:
    raise HTTPException(501, "not (yet) implemented")
