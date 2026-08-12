"""
Intelligence Provider.

Provides intelligence services for DoodleTurtleAI.
"""

from doodleturtle.intelligence.response import IntelligenceResponse


class IntelligenceProvider:
    """Base intelligence provider."""

    def __init__(self) -> None:
        """Initialize the provider."""
        self._name = "Internal"

    @property
    def name(self) -> str:
        """Return the provider name."""
        return self._name

    def generate(
        self,
        prompt: str,
        context: str,
    ) -> IntelligenceResponse:
        """Generate an intelligence response."""
        content = (
            "Intelligence services are not yet connected.\n\n"
            "Prompt\n"
            "------\n"
            f"{prompt}\n\n"
            "Knowledge Context\n"
            "-----------------\n"
            f"{context}"
        )

        return IntelligenceResponse(
            content=content,
            provider=self._name,
        )