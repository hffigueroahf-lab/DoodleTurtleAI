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

    def create_project(
        self,
        name: str,
        category: str,
    ) -> DoodleProject:
        """Create and register a new project."""
        project = DoodleProject(
            name=name,
            category=category,
        )

        self._registry.register_project(project)

        return project

    def add_project(
        self,
        project: DoodleProject,
    ) -> None:
        """Add an existing project."""
        self._registry.register_project(project)

    def start_project(self, name: str) -> bool:
        """Start a project by name."""
        project = self._registry.find_project(name)

        if project is None:
            return False

        project.start()
        return True

    def complete_project(self, name: str) -> bool:
        """Complete a project by name."""
        project = self._registry.find_project(name)

        if project is None:
            return False

        project.complete()
        return True

    def projects(self) -> list[DoodleProject]:
        """Return all projects."""
        return self._registry.projects()

    def planning_projects(self) -> list[DoodleProject]:
        """Return planning projects."""
        return self._registry.planning_projects()

    def active_projects(self) -> list[DoodleProject]:
        """Return active projects."""
        return self._registry.active_projects()

    def completed_projects(self) -> list[DoodleProject]:
        """Return completed projects."""
        return self._registry.completed_projects()

    def projects_by_category(
        self,
        category: str,
    ) -> list[DoodleProject]:
        """Return projects matching a category."""
        return self._registry.projects_by_category(category)

    def project_count(self) -> int:
        """Return the number of registered projects."""
        return self._registry.project_count()