from pydantic_settings import BaseSettings
from weaviate.auth import AuthCredentials
from weaviate.config import AdditionalConfig
from typing import Dict, Optional

class WeaviateSettings(BaseSettings):
    http_host: str
    http_port: int
    http_secure: bool
    grpc_host: str
    grpc_port: int
    grpc_secure: bool
    headers: Optional[Dict[str, str]] = None
    additional_config: Optional[AdditionalConfig] = None
    auth_credentials: Optional[AuthCredentials] = None
    skip_init_checks: bool = False
