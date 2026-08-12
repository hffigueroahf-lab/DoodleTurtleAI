"""
Doodle Project.

Represents a DoodleTurtleCo project.
"""


class DoodleProject:
    """Represent a DoodleTurtleCo project."""

    def __init__(
        self,
        name: str,
        category: str,
        status: str = "Planning",
    ) -> None:
        """Initialize a project."""
        self._name = name
        self._category = category
        self._status = status

    @property
    def name(self) -> str:
        """Return the project name."""
        return self._name

    @property
    def category(self) -> str:
        """Return the project category."""
        return self._category

    @property
    def status(self) -> str:
        """Return the project status."""
        return self._status

    def start(self) -> None:
        """Mark the project as active."""
        self._status = "Active"

    def complete(self) -> None:
        """Mark the project as complete."""
        self._status = "Complete"