"""
Integration test for the KnowledgeLoader.
"""

from doodleturtle.knowledge.loader import KnowledgeLoader


def main() -> None:
    """Test knowledge document discovery."""
    loader = KnowledgeLoader()

    documents = loader.discover_documents()

    print()
    print("========================================")
    print("Knowledge Library")
    print("========================================")

    for document in documents:
        print(document.relative_to(loader._repository_root))

    print("----------------------------------------")
    print(f"Total Documents: {len(documents)}")
    print("========================================")


if __name__ == "__main__":
    main()