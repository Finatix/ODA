"""service for the LLM
"""

from ..components.ai import OpenAiSettings
from .openai_settings import openai_settings
from fastapi import Depends
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from typing import Annotated

def chat_model(settings: Annotated[OpenAiSettings, Depends(openai_settings)]) -> BaseChatModel:
    return ChatOpenAI(settings.llm_name)
