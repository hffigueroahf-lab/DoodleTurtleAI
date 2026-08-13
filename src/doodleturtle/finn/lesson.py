"""
Finn Lesson.

Represents a structured educational lesson.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FinnLesson:
    """Represent a lesson created by Finn."""

    title: str

    topic: str

    learning_objective: str

    introduction: str

    explanation: str

    curiosity_prompt: str

    closing: str