"""
Finn Engine.

Represents Finn, the educational guide for DoodleTurtleAI.
"""

from doodleturtle.finn.principles import FinnPrinciples
from doodleturtle.finn.voice import FinnVoice
from doodleturtle.knowledge.library import KnowledgeLibrary


class Finn:
    """Represent Finn, the educational guide."""

    def __init__(self, knowledge: KnowledgeLibrary) -> None:
        """Initialize Finn."""
        self._knowledge = knowledge
        self._principles = FinnPrinciples(knowledge)
        self._voice = FinnVoice(self._principles)

    @property
    def name(self) -> str:
        """Return Finn's name."""
        return "Finn"

    @property
    def introduction(self) -> str:
        """Return Finn's introduction."""
        return (
            "Hi! I'm Finn. I love asking questions, exploring the world, "
            "and learning together. If we don't know the answer yet, "
            "let's find out together."
        )

    @property
    def personality(self) -> str:
        """Return Finn's personality profile."""
        return self._knowledge.get("finn")

    @property
    def principles(self) -> FinnPrinciples:
        """Return Finn's educational principles."""
        return self._principles

    @property
    def voice(self) -> FinnVoice:
        """Return Finn's communication style."""
        return self._voice

    def teach(self, topic: str) -> str:
        """Begin a learning experience about a topic."""
        return (
            f"{self.voice.greeting}\n\n"
            f"Today, let's explore: {topic}\n\n"
            "We'll ask questions, discover together, "
            "and enjoy learning one step at a time."
        )