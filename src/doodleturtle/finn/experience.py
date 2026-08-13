"""
Finn Educational Experience.

Represents a complete learning experience
created from a Finn lesson.
"""

from dataclasses import dataclass

from doodleturtle.finn.lesson import FinnLesson
from doodleturtle.finn.templates import EducationalTemplate


@dataclass(frozen=True)
class FinnExperience:
    """Represent an educational experience."""

    lesson: FinnLesson

    template: EducationalTemplate

    fun_fact: str

    activity: str

    reflection: str