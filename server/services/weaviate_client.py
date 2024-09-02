"""service definition for the weaviate client
"""

from ..components.weaviate import WeaviateSettings
from .weaviate_settings import weaviate_settings
from fastapi import Depends
from typing import Annotated
from weaviate import  WeaviateClient
from weaviate.connect import ConnectionParams, ProtocolParams

def weaviate_client(settings: Annotated[WeaviateSettings, Depends(weaviate_settings)]) -> WeaviateClient:

    http = ProtocolParams(host=settings.http_host, port=settings.http_port, secure=settings.http_secure)
    grpc = ProtocolParams(host=settings.grpc_host, port=settings.grpc_port, secure=settings.grpc_secure)

    connection = ConnectionParams(http=http, grpc=grpc)

    return WeaviateClient(
        connection_params=connection,
        auth_client_secret=settings.auth_credentials,
        additional_headers=settings.headers,
        additional_config=settings.additional_config,
        skip_init_checks=settings.skip_init_checks
    )
