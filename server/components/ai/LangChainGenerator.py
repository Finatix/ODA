"""implementation of Generator with LangChain
"""

from ..models import Conversation
from . import Generator
from typing import override

class LangChainGenerator(Generator):
    """implementation of Generator with LangChain
    """

    @override
    def generate(self, prompt: str, conversation: Conversation) -> str:
        pass
