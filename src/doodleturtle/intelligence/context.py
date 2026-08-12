"""
Knowledge Context Builder.

Builds knowledge context for intelligence requests.
"""

from doodleturtle.knowledge.library import KnowledgeLibrary


class KnowledgeContextBuilder:
    """Build knowledge context from the Knowledge Library."""

    def __init__(
        self,
        knowledge: KnowledgeLibrary,
    ) -> None:
        """Initialize the context builder."""
        self._knowledge = knowledge

    def build(
        self,
        documents: list[str],
    ) -> str:
        """Build a combined knowledge context."""
        sections: list[str] = []

        for document in documents:
            sections.append(self._knowledge.get(document))

        return "\n\n".join(sections)