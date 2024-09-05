"""service definitions for weaviate settings
"""

from ..settings import Weaviate
from functools import lru_cache
from os import getenv

@lru_cache
def weaviate_settings() -> Weaviate:
    return Weaviate(
        http_host=getenv("WEAVIATE_HTTP_HOST", "0.0.0.0"),
        http_port=getenv("WEAVIATE_HTTP_PORT", 9090),
        http_secure=getenv("WEAVIATE_HTTP_SECURE", False),
        grpc_host=getenv("WEAVIATE_GRPC_HOST", getenv("WEAVIATE_HTTP_HOST", "0.0.0.0")),
        grpc_port=getenv("WEAVIATE_GRPC_PORT", 50051),
        grpc_secure=getenv("WEAVIATE_GRPC_SECURE", False),
        skip_init_checks=True
    )
