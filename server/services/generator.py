"""service for the text generator
"""

from ..components.ai import Generator, LangChainGenerator

def generator() -> Generator:
    """creates the Generator service

    Returns:
        Generator: the service to be injected
    """
    return LangChainGenerator()
