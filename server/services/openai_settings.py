"""service definition fror OpenAI settings
"""

from ..settings import OpenAi
from functools import lru_cache
from os import getenv

@lru_cache
def openai_settings() -> OpenAi:
    return OpenAi(
        api_key=getenv("OPENAI_API_KEY"),
        llm_name=getenv("OPENAI_MODEL")
    )
