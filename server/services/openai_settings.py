"""service definition fror OpenAI settings
"""

from ..components.ai import OpenAiSettings
from os import getenv

def openai_settings() -> OpenAiSettings:
    return OpenAiSettings(
        api_key=getenv("OPENAI_API_KEY"),
        llm_name=getenv("OPENAI_MODEL")
    )
