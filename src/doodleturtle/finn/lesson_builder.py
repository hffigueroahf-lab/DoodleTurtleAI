"""
Finn Lesson Builder.

Transforms intelligence responses into structured lessons.
"""

from doodleturtle.finn.lesson import FinnLesson
from doodleturtle.intelligence.response import IntelligenceResponse


class FinnLessonBuilder:
    """Build structured educational lessons."""

    def build(
        self,
        response: IntelligenceResponse,
    ) -> FinnLesson:
        """Build a lesson from an intelligence response."""

        return FinnLesson(
            title="Learning Together",
            topic="general",
            learning_objective=(
                "Help the learner understand one new idea, "
                "feel confident asking questions, and become "
                "more curious about the world."
            ),
            introduction=(
                "That's a wonderful question! "
                "Let's explore it together."
            ),
            explanation=response.content,
            curiosity_prompt=(
                "What do you think might happen next?"
            ),
            closing=(
                "Keep asking questions. "
                "Curiosity helps us discover amazing things!"
            ),
        )