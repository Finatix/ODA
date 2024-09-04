from pydantic_settings import BaseSettings
from typing import Annotated

class OpenAi(BaseSettings):
    llm_name: Annotated[str, "name of the LLM used with OpenAI"]
    api_key: Annotated[str, "OpenAI API key"]
