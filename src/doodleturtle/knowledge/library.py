"""
Knowledge library for DoodleTurtleAI.

Provides organized access to the Knowledge Library.
"""

from pathlib import Path

from doodleturtle.knowledge.loader import KnowledgeLoader


class KnowledgeLibrary:
    """Provide organized access to knowledge documents."""

    def __init__(self) -> None:
        """Initialize the Knowledge Library."""
        self._loader = KnowledgeLoader()
        self._documents = self._loader.discover_documents()

        self._document_index: dict[str, Path] = {
            document.stem: document
            for document in self._documents
        }

    def documents(self) -> list[Path]:
        """Return all discovered knowledge documents."""
        return self._documents

    def get(self, name: str) -> str:
        """Return the contents of a knowledge document by name."""
        document = self._document_index.get(name)

        if document is None:
            raise ValueError(f"Knowledge document '{name}' was not found.")

        return self._loader.load_document(document)