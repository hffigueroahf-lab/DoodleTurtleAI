"""
Intelligence Provider.

Defines the interface implemented by all intelligence providers.
"""

from abc import ABC, abstractmethod

from doodleturtle.intelligence.response import IntelligenceResponse


class IntelligenceProvider(ABC):
    """Abstract base class for intelligence providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the provider name."""

    @abstractmethod
    def answer(
        self,
        prompt: str,
        context: str,
    ) -> IntelligenceResponse:
        """Generate an intelligence response."""