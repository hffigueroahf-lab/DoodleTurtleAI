"""
Finn Response Builder.

Formats educational experiences into conversational responses.
"""

from doodleturtle.finn.experience import FinnExperience
from doodleturtle.finn.messages import (
    CELEBRATION,
    CREATE,
    EXPLORE,
    LEARN,
    REFLECT,
    WELCOME,
    WONDER,
)


class FinnResponseBuilder:
    """Present educational experiences as conversations."""

    def build(
        self,
        experience: FinnExperience,
    ) -> str:
        """Build a conversational response."""

        lesson = experience.lesson

        return (
            f"{WELCOME}\n\n"
            f"{WONDER}\n\n"
            f"{LEARN}\n\n"
            f"{lesson.explanation}\n\n"
            f"{EXPLORE}\n\n"
            f"{experience.fun_fact}\n\n"
            f"{CREATE}\n\n"
            f"{experience.activity}\n\n"
            f"{REFLECT}\n\n"
            f"{experience.reflection}\n\n"
            f"{CELEBRATION}\n\n"
            f"{lesson.closing}"
        )