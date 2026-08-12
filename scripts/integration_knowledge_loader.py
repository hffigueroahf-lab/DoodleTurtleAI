"""
Integration test for the Knowledge Library.
"""

from doodleturtle.knowledge.library import KnowledgeLibrary


def main() -> None:
    """Test retrieving knowledge documents."""
    library = KnowledgeLibrary()

    print()
    print("========================================")
    print("Mission")
    print("========================================")
    print(library.get("mission"))

    print()
    print("========================================")
    print("Finn")
    print("========================================")
    print(library.get("finn"))


if __name__ == "__main__":
    main()