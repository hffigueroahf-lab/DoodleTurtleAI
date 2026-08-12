"""
Knowledge Context Strategies.

Define reusable knowledge context strategies.
"""


class ContextStrategy:
    """Provide document selections for intelligence contexts."""

    def documents(
        self,
        strategy: str,
    ) -> list[str]:
        """Return the documents for a strategy."""
        strategies = {
            "finn": [
                "mission",
                "vision",
                "child_first",
            ],
            "operations": [
                "mission",
                "vision",
            ],
        }

        return strategies.get(strategy, [])