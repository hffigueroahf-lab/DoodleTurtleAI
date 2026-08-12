"""
Integration test for the Finn Engine.
"""

from doodleturtle.finn import FinnEngine
from doodleturtle.knowledge.library import KnowledgeLibrary


def main() -> None:
    """Run the Finn Engine integration test."""
    knowledge = KnowledgeLibrary()

    finn = FinnEngine(
        knowledge=knowledge,
    )

    print("# Finn Engine")
    print()

    print("## Name")
    print()
    print("Finn")
    print()

    print("## Greeting")
    print()
    print(finn.voice.greeting)
    print()

    print("## Tone")
    print()
    print(finn.voice.tone)
    print()

    question = "Why is curiosity important?"

    print("## Question")
    print()
    print(question)
    print()

    answer = finn.answer(question)

    print("## Finn's Response")
    print()
    print(answer)
    print()

    print("## Closing")
    print()
    print(finn.voice.closing)


if __name__ == "__main__":
    main()