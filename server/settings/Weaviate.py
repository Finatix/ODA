from pydantic import Field
from pydantic_settings import BaseSettings
from weaviate.auth import AuthCredentials
from weaviate.config import AdditionalConfig
from typing import Annotated, Dict, Optional

class Weaviate(BaseSettings):
    http_host: str
    http_port: int
    http_secure: bool
    grpc_host: str
    grpc_port: int
    grpc_secure: bool
    headers: Annotated[Optional[Dict[str, str]], Field(exclude=True)] = None
    additional_config: Annotated[Optional[AdditionalConfig], Field(exclude=True)] = None
    auth_credentials: Annotated[Optional[AuthCredentials], Field(exclude=True)] = None
    skip_init_checks: Annotated[bool, Field(exclude=True)] = False
