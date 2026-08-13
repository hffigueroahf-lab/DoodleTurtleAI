"""
Finn Experience Builder.

Transforms lessons into complete educational experiences.
"""

from doodleturtle.finn.experience import FinnExperience
from doodleturtle.finn.lesson import FinnLesson
from doodleturtle.finn.templates import NATURE_TEMPLATE


class FinnExperienceBuilder:
    """Build educational experiences from lessons."""

    def build(
        self,
        lesson: FinnLesson,
    ) -> FinnExperience:
        """Build an educational experience."""

        return FinnExperience(
            lesson=lesson,
            template=NATURE_TEMPLATE,
            fun_fact=self._build_fun_fact(lesson),
            activity=self._build_activity(lesson),
            reflection=self._build_reflection(lesson),
        )

    def _build_fun_fact(
        self,
        lesson: FinnLesson,
    ) -> str:
        """Build a lesson-specific fun fact."""
        topic = lesson.topic.lower()

        if "turtle" in topic:
            return (
                "Sea turtles can travel thousands of miles "
                "and often return to the same nesting beach."
            )

        return (
            "Every time we learn something new, our understanding "
            "of the world grows a little stronger."
        )

    def _build_activity(
        self,
        lesson: FinnLesson,
    ) -> str:
        """Build a lesson-specific activity."""
        topic = lesson.topic.lower()

        if "turtle" in topic:
            return (
                "Draw a sea turtle's journey from the beach "
                "to the ocean and back again."
            )

        return (
            "Draw or write one thing you learned today "
            "and share it with someone you care about."
        )

    def _build_reflection(
        self,
        lesson: FinnLesson,
    ) -> str:
        """Build a lesson-specific reflection."""
        topic = lesson.topic.lower()

        if "turtle" in topic:
            return (
                "Why do you think sea turtles remember "
                "where they were born?"
            )

        return (
            "What new question do you have after "
            "today's lesson?"
        )