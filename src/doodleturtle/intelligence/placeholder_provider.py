"""
Placeholder Intelligence Provider.

Provides a temporary intelligence provider until a live
AI provider is connected.
"""

from doodleturtle.intelligence.provider import IntelligenceProvider
from doodleturtle.intelligence.response import IntelligenceResponse


class PlaceholderProvider(IntelligenceProvider):
    """Provide placeholder intelligence responses."""

    @property
    def name(self) -> str:
        """Return the provider name."""
        return "Placeholder"

    def answer(
        self,
        prompt: str,
        context: str,
    ) -> IntelligenceResponse:
        """Return a placeholder response."""

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
            provider=self.name,
        )