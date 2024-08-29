from .components.conversation import ConversationManager, MockConversationManager

def conversation_manager() -> ConversationManager:
    return MockConversationManager()

__all__ = [
    "ConversationManager"
    "coversation_manager"
]
