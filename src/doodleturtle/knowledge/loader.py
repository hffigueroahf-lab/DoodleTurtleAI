"""
Knowledge loader for DoodleTurtleAI.

Responsible for reading Markdown knowledge files.
"""

from pathlib import Path


class KnowledgeLoader:
    """Load knowledge documents from the Knowledge Library."""

    def __init__(self) -> None:
        """Initialize the Knowledge Loader."""
        self._module_path = Path(__file__).resolve()
        self._repository_root = self._module_path.parents[3]

    def discover_documents(self) -> list[Path]:
        """Discover all Markdown documents in the Knowledge Library."""
        knowledge_path = self._repository_root / "knowledge"

        return sorted(knowledge_path.rglob("*.md"))