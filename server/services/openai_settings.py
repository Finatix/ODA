"""service definition fror OpenAI settings
"""

from ..settings import OpenAi
from os import getenv

def openai_settings() -> OpenAi:
    return OpenAi(
        api_key=getenv("OPENAI_API_KEY"),
        llm_name=getenv("OPENAI_MODEL")
    )
