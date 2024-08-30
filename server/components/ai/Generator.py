"""interface for text generation
"""

from ..api import Conversation
from abc import ABC, abstractmethod

class Generator(ABC):
    """interface class for text generation
    """

    @abstractmethod
    def generate(self, prompt: str, conversation: Conversation) -> str:
        """generate some text answer to the prompt

        Args:
            prompt (str): the text prompt from the user
            conversation (Conversation): the whole conversation until now

        Returns:
            str: the text answer of the LLM
        """
        pass
