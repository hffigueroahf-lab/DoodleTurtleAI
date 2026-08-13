"""
Finn Journey Builder.

Transforms educational experiences into guided
learning journeys.
"""

from doodleturtle.finn.experience import FinnExperience
from doodleturtle.finn.journey import FinnJourney


class FinnJourneyBuilder:
    """Build guided learning journeys."""

    def build(
        self,
        experience: FinnExperience,
    ) -> FinnJourney:
        """Build a learning journey."""

        lesson = experience.lesson

        return FinnJourney(
            wonder=(
                "🌟 I love that question! "
                "Let's discover something amazing together."
            ),
            learn=lesson.explanation,
            explore=experience.fun_fact,
            create=experience.activity,
            reflect=experience.reflection,
            celebrate=(
                "🎉 Great job exploring today! "
                "Every question you ask helps you become an even better learner."
            ),
        )