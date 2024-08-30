from ..api import PastConversation
from .ConversationManager import ConversationManager, UUID
from typing import override

class MockConversationManager(ConversationManager):
    """
    mock implementation of ConversationManager
    """

    def __init__(self):
        self.__titles: dict[UUID, str]

    @override
    def get_past_conversation(self, token: UUID) -> PastConversation | None:

        title = self.__get_title(token)

        return PastConversation(title=title, id=token)

    @override
    def start_conversation(self) -> UUID:

        return super().start_conversation()


    def __get_title(self, token: UUID) -> str:
        if not token in self.__titles:
            index = len(self.__titles) + 1
            self.__titles[UUID] = f"Conversation {index}"

        return self.__titles[UUID]
