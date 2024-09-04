"""service definition for all application settings
"""

from ..settings import App, OpenAi, Weaviate
from .openai_settings import openai_settings
from .weaviate_settings import weaviate_settings
from fastapi import Depends
from typing import Annotated

def app_settings(
        open_ai: Annotated[OpenAi, Depends(openai_settings)],
        weaviate: Annotated[Weaviate, Depends(weaviate_settings)]
    ) -> App:
    return App(open_ai=open_ai, weaviate=weaviate)
