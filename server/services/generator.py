"""service for the text generator
"""

from ..components.ai import Generator, MockGenerator

def generator() -> Generator:
    """creates the Generator service

    For starters its just the MockGenerator

    Returns:
        Generator: the service to be injected
    """
    return MockGenerator()
