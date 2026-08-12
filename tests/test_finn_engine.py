"""
Tests for the Finn Engine.
"""

from doodleturtle.finn import FinnEngine
from doodleturtle.knowledge.library import KnowledgeLibrary


def test_finn_engine_answers_question() -> None:
    """Verify Finn can answer a question."""
    knowledge = KnowledgeLibrary()

    finn = FinnEngine(
        knowledge=knowledge,
    )

    answer = finn.answer(
        "Why is curiosity important?"
    )

    assert "That's a wonderful question!" in answer

    assert "Curiosity helps us discover amazing things!" in answer