"""
Operations Registry.

Maintains information about DoodleTurtleCo projects.
"""

from doodleturtle.operations.project import DoodleProject


class OperationsRegistry:
    """Registry of DoodleTurtleCo projects."""

    def __init__(self) -> None:
        """Initialize the registry."""
        self._projects: list[DoodleProject] = []

    def register_project(self, project: DoodleProject) -> None:
        """Register a project."""
        if project not in self._projects:
            self._projects.append(project)

    def projects(self) -> list[DoodleProject]:
        """Return all registered projects."""
        return sorted(
            self._projects,
            key=lambda project: project.name,
        )

    def project_count(self) -> int:
        """Return the number of registered projects."""
        return len(self._projects)