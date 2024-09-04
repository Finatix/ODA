from abc import ABC, abstractmethod
from langchain_core.language_models import BaseChatModel

class Factory(ABC):

    @abstractmethod
    def chat_model() -> BaseChatModel:
        raise NotImplementedError()
