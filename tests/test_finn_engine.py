"""
Tests for the Finn Engine.
"""

from doodleturtle.finn import FinnEngine
from doodleturtle.knowledge.library import KnowledgeLibrary


def test_finn_engine_answers_question() -> None:
    """Verify Finn produces a complete educational response."""

    knowledge = KnowledgeLibrary()

    finn = FinnEngine(
        knowledge=knowledge,
    )

    answer = finn.answer(
        "Why is curiosity important?"
    )

    assert "WELCOME" in answer
    assert "WONDER" in answer
    assert "LEARN" in answer
    assert "EXPLORE" in answer
    assert "CREATE" in answer
    assert "REFLECT" in answer
    assert "CELEBRATE" in answer

    assert "Curiosity helps us discover amazing things!" in answer