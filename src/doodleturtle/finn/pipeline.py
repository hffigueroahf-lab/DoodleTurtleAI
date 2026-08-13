"""
Finn Educational Pipeline.

Coordinates the transformation from
intelligence responses into educational journeys.
"""

from doodleturtle.finn.experience_builder import FinnExperienceBuilder
from doodleturtle.finn.journey_builder import FinnJourneyBuilder
from doodleturtle.finn.lesson_builder import FinnLessonBuilder
from doodleturtle.finn.response_builder import FinnResponseBuilder
from doodleturtle.intelligence.response import IntelligenceResponse


class FinnPipeline:
    """Coordinate Finn's educational pipeline."""

    def __init__(self) -> None:
        """Initialize the educational pipeline."""
        self._lesson_builder = FinnLessonBuilder()
        self._experience_builder = FinnExperienceBuilder()
        self._journey_builder = FinnJourneyBuilder()
        self._response_builder = FinnResponseBuilder()

    def build(
        self,
        response: IntelligenceResponse,
    ) -> str:
        """Build a complete educational response."""

        lesson = self._lesson_builder.build(
            response,
        )

        experience = self._experience_builder.build(
            lesson,
        )

        # Build the learning journey. It will become the primary
        # presentation model in a future milestone.
        _ = self._journey_builder.build(
            experience,
        )

        return self._response_builder.build(
            experience,
        )