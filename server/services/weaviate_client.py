"""service definition for the weaviate client
"""

from ..components.weaviate import WeaviateSettings
from .weaviate_settings import weaviate_settings
from fastapi import Depends
from typing import Annotated
from weaviate import  WeaviateClient
from weaviate.connect import ConnectionParams, ProtocolParams

def weaviate_client(settings: Annotated[WeaviateSettings, Depends(weaviate_settings)]) -> WeaviateClient:
    params = settings.model_dump()
    connection = ConnectionParams.from_params(**params)

    return WeaviateClient(
        connection_params=connection,
        auth_client_secret=settings.auth_credentials,
        additional_headers=settings.headers,
        additional_config=settings.additional_config,
        skip_init_checks=settings.skip_init_checks
    )
