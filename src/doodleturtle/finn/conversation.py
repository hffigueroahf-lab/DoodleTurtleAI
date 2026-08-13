"""
Finn Conversation.

Coordinates educational conversations using the
Intelligence Service.
"""

from doodleturtle.finn.experience_builder import FinnExperienceBuilder
from doodleturtle.finn.lesson_builder import FinnLessonBuilder
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
        self._lesson_builder = FinnLessonBuilder()
        self._experience_builder = FinnExperienceBuilder()
        self._response_builder = FinnResponseBuilder()

    def answer(
        self,
        question: str,
    ) -> str:
        """Answer a child's question."""

        intelligence_response = self._intelligence.generate(
            prompt=question,
            strategy="finn",
        )

        lesson = self._lesson_builder.build(
            intelligence_response,
        )

        experience = self._experience_builder.build(
            lesson,
        )

        return self._response_builder.build(
            experience,
        )