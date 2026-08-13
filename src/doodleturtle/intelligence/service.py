"""
Intelligence Service.

Coordinates intelligence providers.
"""

from doodleturtle.intelligence.context import KnowledgeContextBuilder
from doodleturtle.intelligence.placeholder_provider import PlaceholderProvider
from doodleturtle.intelligence.provider import IntelligenceProvider
from doodleturtle.intelligence.response import IntelligenceResponse
from doodleturtle.intelligence.strategy import ContextStrategy
from doodleturtle.knowledge.library import KnowledgeLibrary


class IntelligenceService:
    """Coordinate intelligence services."""

    def __init__(
        self,
        knowledge: KnowledgeLibrary,
        provider: IntelligenceProvider | None = None,
    ) -> None:
        """Initialize the intelligence service."""
        self._context = KnowledgeContextBuilder(knowledge)
        self._strategy = ContextStrategy()
        self._provider = provider or PlaceholderProvider()

    @property
    def provider(self) -> IntelligenceProvider:
        """Return the intelligence provider."""
        return self._provider

    def generate(
        self,
        prompt: str,
        strategy: str,
    ) -> IntelligenceResponse:
        """Generate an intelligence response."""
        documents = self._strategy.documents(strategy)

        context = self._context.build(
            documents,
        )

        return self._provider.answer(
            prompt=prompt,
            context=context,
        )