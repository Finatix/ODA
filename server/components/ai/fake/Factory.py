from langchain_core.language_models import BaseChatModel
from langchain_core.language_models.fake_chat_models import ParrotFakeChatModel
from ..Factory import Factory as BaseFactory
from typing import override

class Factory(BaseFactory):

    @override
    def chat_model() -> BaseChatModel:
        return ParrotFakeChatModel()
