"""
Tests for the Intelligence Service.
"""

from doodleturtle.intelligence import IntelligenceService
from doodleturtle.knowledge.library import KnowledgeLibrary


def test_intelligence_service_generates_response() -> None:
    """Verify the Intelligence Service returns a response."""
    knowledge = KnowledgeLibrary()

    intelligence = IntelligenceService(
        knowledge=knowledge,
    )

    response = intelligence.generate(
        prompt="Why is curiosity important?",
        strategy="finn",
    )

    assert response.provider == "Internal"

    assert (
        "Why is curiosity important?"
        in response.content
    )

    assert (
        "Our Mission"
        in response.content
    )