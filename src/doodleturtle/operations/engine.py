"""
Operations Engine.

Coordinates operational services for DoodleTurtleAI.
"""

from doodleturtle.operations.project import DoodleProject
from doodleturtle.operations.registry import OperationsRegistry


class OperationsEngine:
    """Coordinate DoodleTurtleAI operations."""

    def __init__(self) -> None:
        """Initialize the Operations Engine."""
        self._registry = OperationsRegistry()

    @property
    def registry(self) -> OperationsRegistry:
        """Return the operations registry."""
        return self._registry

    def add_project(self, project: DoodleProject) -> None:
        """Add a project to the registry."""
        self._registry.register_project(project)

    def project_count(self) -> int:
        """Return the number of registered projects."""
        return self._registry.project_count()

    def projects(self) -> list[DoodleProject]:
        """Return all registered projects."""
        return self._registry.projects()