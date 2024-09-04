"""service for the chat model
"""
from ..components.ai import Factory
from .ai_factory import ai_factory
from fastapi import Depends
from langchain_core.language_models import BaseChatModel
from typing import Annotated

def chat_model(factory: Annotated[Factory, Depends(ai_factory)]) -> BaseChatModel:
    return factory.chat_model()
