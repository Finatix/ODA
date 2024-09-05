"""service for the text generator
"""

from ..components.ai import Generator, LangChainGenerator
from .weaviate_client import weaviate_client
from fastapi import Depends
from functools import lru_cache
from typing import Annotated
from weaviate import WeaviateClient

@lru_cache
def generator(weaviate_client: Annotated[WeaviateClient, Depends(weaviate_client)]) -> Generator:
    """creates the Generator service

    Returns:
        Generator: the service to be injected
    """
    return LangChainGenerator(weaviate_client)
