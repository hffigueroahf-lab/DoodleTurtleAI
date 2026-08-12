"""
Finn's Core Principles.

These principles represent the educational philosophy that guides
every interaction Finn has with children.
"""

from doodleturtle.knowledge.library import KnowledgeLibrary


class FinnPrinciples:
    """Represent Finn's educational principles."""

    def __init__(self, knowledge: KnowledgeLibrary) -> None:
        """Initialize Finn's principles."""
        self._knowledge = knowledge

    @property
    def child_first(self) -> str:
        """Return the Child First philosophy."""
        return self._knowledge.get("child_first")

    @property
    def teaching_principles(self) -> str:
        """Return Finn's teaching principles."""
        return self._knowledge.get("teaching_principles")

    @property
    def mission(self) -> str:
        """Return the project mission."""
        return self._knowledge.get("mission")

    @property
    def vision(self) -> str:
        """Return the project vision."""
        return self._knowledge.get("vision")

    def emotional_safety(self) -> bool:
        """Children should always feel emotionally safe."""
        return True

    def teaches_beside(self) -> bool:
        """Finn teaches beside children, never above them."""
        return True

    def encourages_curiosity(self) -> bool:
        """Curiosity should always be encouraged."""
        return True

    def celebrates_mistakes(self) -> bool:
        """Mistakes are part of learning."""
        return True

    def uses_illustration(self) -> bool:
        """Illustration is preferred whenever it improves understanding."""
        return True