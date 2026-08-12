"""
Integration test for the Intelligence Service.
"""

from doodleturtle.intelligence import IntelligenceService
from doodleturtle.knowledge.library import KnowledgeLibrary


def main() -> None:
    """Run the Intelligence Service integration test."""
    knowledge = KnowledgeLibrary()

    intelligence = IntelligenceService(
        knowledge=knowledge,
    )

    response = intelligence.generate(
        prompt="Explain why curiosity is important for children.",
        strategy="finn",
    )

    print("# Intelligence Service")
    print()

    print("## Provider")
    print()
    print(response.provider)
    print()

    print("## Strategy")
    print()
    print("finn")
    print()

    print("## Response")
    print()
    print(response.content)


if __name__ == "__main__":
    main()