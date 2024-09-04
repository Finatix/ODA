from .OpenAi import OpenAi
from .Weaviate import Weaviate
from pydantic_settings import BaseSettings
from typing import Annotated

class App(BaseSettings):
    open_ai: Annotated[OpenAi, "OpenAI settings"]
    weaviate: Annotated[Weaviate, "Weaviate settings"]
