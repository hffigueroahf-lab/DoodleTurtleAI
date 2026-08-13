"""
Finn Learning Journey.

Represents the stages of an educational experience.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FinnJourney:
    """Represent a guided learning journey."""

    wonder: str

    learn: str

    explore: str

    create: str

    reflect: str

    celebrate: str