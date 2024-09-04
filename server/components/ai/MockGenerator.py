"""mock implementation of Generator
"""

from ..models import Conversation
from . import Generator
from typing import override

class MockGenerator(Generator):
    """mock implementation of Generator
    """

    @override
    def generate(self, prompt: str, conversation: Conversation) -> str:
        return prompt[::-1]
