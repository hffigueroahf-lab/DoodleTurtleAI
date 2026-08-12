"""
Knowledge package for DoodleTurtleAI.
"""

from doodleturtle.knowledge.library import KnowledgeLibrary


def initialize_knowledge() -> KnowledgeLibrary:
    """Initialize the Knowledge Library."""
    library = KnowledgeLibrary()

    print(f"Loaded {library.count()} knowledge documents.")

    return library