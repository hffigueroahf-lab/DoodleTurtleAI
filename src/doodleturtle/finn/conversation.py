"""
Finn Conversation.

Coordinates educational conversations using the
Intelligence Service.
"""

from doodleturtle.finn.response_builder import FinnResponseBuilder
from doodleturtle.intelligence import IntelligenceService


class FinnConversation:
    """Coordinate Finn conversations."""

    def __init__(
        self,
        intelligence: IntelligenceService,
    ) -> None:
        """Initialize the conversation."""
        self._intelligence = intelligence
        self._builder = FinnResponseBuilder()

    def answer(
        self,
        question: str,
    ) -> str:
        """Answer a child's question."""
        response = self._intelligence.generate(
            prompt=question,
            strategy="finn",
        )

        return self._builder.build(response)