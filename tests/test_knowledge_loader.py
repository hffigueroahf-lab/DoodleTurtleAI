"""
Automated tests for the Knowledge Library.
"""

from doodleturtle.knowledge.library import KnowledgeLibrary


def test_knowledge_library_counts_documents() -> None:
    """Verify the Knowledge Library loads all knowledge documents."""
    library = KnowledgeLibrary()

    assert library.count() == 6