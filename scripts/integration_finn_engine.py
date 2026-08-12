"""
Integration test for the Finn Engine.
"""

from doodleturtle.finn import Finn
from doodleturtle.knowledge.library import KnowledgeLibrary


def main() -> None:
    """Run the Finn integration test."""
    knowledge = KnowledgeLibrary()
    finn = Finn(knowledge)

    print("# Finn Engine")
    print()

    print("Name")
    print("----")
    print(finn.name)
    print()

    print("Introduction")
    print("------------")
    print(finn.introduction)
    print()

    print("Teaching Demo")
    print("-------------")
    print(finn.teach("Why do sea turtles migrate?"))
    print()

    print("Mission")
    print("-------")
    print(finn.principles.mission[:200])
    print()

    print("Voice")
    print("-----")
    print(f"Greeting: {finn.voice.greeting}")
    print()
    print(f"Tone: {finn.voice.tone}")
    print()
    print(f"Closing: {finn.voice.closing}")
    print()

    print("Behavior")
    print("--------")
    print(f"Encourages Questions: {finn.voice.encourages_questions()}")
    print(f"Celebrates Curiosity: {finn.voice.celebrates_curiosity()}")
    print(f"Emotional Safety:     {finn.voice.protects_emotional_safety()}")
    print(f"Simple Language:      {finn.voice.uses_simple_language()}")
    print(f"Ends Encouragingly:   {finn.voice.ends_with_encouragement()}")


if __name__ == "__main__":
    main()