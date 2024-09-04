"""service definition for the abstrct factory of AI objects
"""

from ..components.ai import Factory as AbstractFactory
from ..components.ai.fake import Factory as FakeFactory

def ai_factory() -> AbstractFactory:
    return FakeFactory()
