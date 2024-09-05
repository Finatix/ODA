"""service for the ConversationManager
"""

from ..components.conversation import ConversationManager, WeaviateConversationManager
from .weaviate_client import weaviate_client
from fastapi import Depends
from functools import lru_cache
from weaviate import WeaviateClient
from typing import Annotated

@lru_cache
def conversation_manager(client: Annotated[WeaviateClient, Depends(weaviate_client)]) -> ConversationManager:
    """creates the ConversationManager service

    Currently it's the WeaviateConversationManager

    Returns:
        ConversationManager: the service to be injected
    """
    return WeaviateConversationManager(client)
