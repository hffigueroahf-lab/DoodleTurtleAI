"""
Finn Engine.

Coordinates Finn's educational services.
"""

from doodleturtle.finn.conversation import FinnConversation
from doodleturtle.finn.principles import FinnPrinciples
from doodleturtle.finn.voice import FinnVoice
from doodleturtle.intelligence import IntelligenceService
from doodleturtle.knowledge.library import KnowledgeLibrary


class FinnEngine:
    """Coordinate Finn's educational behavior."""

    def __init__(
        self,
        knowledge: KnowledgeLibrary,
    ) -> None:
        """Initialize the Finn Engine."""
        self._knowledge = knowledge

        self._principles = FinnPrinciples(
            knowledge=self._knowledge,
        )

        self._voice = FinnVoice(
            principles=self._principles,
        )

        intelligence = IntelligenceService(
            knowledge=self._knowledge,
        )

        self._conversation = FinnConversation(
            intelligence=intelligence,
        )

    @property
    def knowledge(self) -> KnowledgeLibrary:
        """Return the knowledge library."""
        return self._knowledge

    @property
    def principles(self) -> FinnPrinciples:
        """Return Finn's teaching principles."""
        return self._principles

    @property
    def voice(self) -> FinnVoice:
        """Return Finn's communication style."""
        return self._voice

    def answer(
        self,
        question: str,
    ) -> str:
        """Answer a child's question."""
        return self._conversation.answer(question)