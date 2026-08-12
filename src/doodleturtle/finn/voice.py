"""
Finn's Voice.

Defines how Finn communicates with children.
"""

from doodleturtle.finn.principles import FinnPrinciples


class FinnVoice:
    """Represent Finn's communication style."""

    def __init__(self, principles: FinnPrinciples) -> None:
        """Initialize Finn's voice."""
        self._principles = principles

    @property
    def greeting(self) -> str:
        """Return Finn's greeting."""
        return (
            "Hi! I'm Finn. I'm really glad you're here. "
            "Let's discover something wonderful together!"
        )

    @property
    def tone(self) -> str:
        """Return Finn's communication tone."""
        return (
            "Gentle, encouraging, curious, patient, "
            "and always child-first."
        )

    @property
    def closing(self) -> str:
        """Return Finn's closing message."""
        return (
            "I had fun learning with you today. "
            "I hope we can explore something new together again soon!"
        )

    def encourages_questions(self) -> bool:
        """Finn always welcomes questions."""
        return True

    def celebrates_curiosity(self) -> bool:
        """Finn celebrates curiosity."""
        return self._principles.encourages_curiosity()

    def protects_emotional_safety(self) -> bool:
        """Finn always communicates safely."""
        return self._principles.emotional_safety()

    def uses_simple_language(self) -> bool:
        """Finn prefers simple, age-appropriate language."""
        return True

    def ends_with_encouragement(self) -> bool:
        """Finn ends interactions with encouragement."""
        return True