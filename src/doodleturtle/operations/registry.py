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
        if self.find_project(project.name) is None:
            self._projects.append(project)

    def find_project(self, name: str) -> DoodleProject | None:
        """Find a project by name."""
        for project in self._projects:
            if project.name == name:
                return project

        return None

    def projects(self) -> list[DoodleProject]:
        """Return all projects."""
        return sorted(
            self._projects,
            key=lambda project: project.name,
        )

    def planning_projects(self) -> list[DoodleProject]:
        """Return projects in planning."""
        return [
            project
            for project in self.projects()
            if project.is_planning
        ]

    def active_projects(self) -> list[DoodleProject]:
        """Return active projects."""
        return [
            project
            for project in self.projects()
            if project.is_active
        ]

    def completed_projects(self) -> list[DoodleProject]:
        """Return completed projects."""
        return [
            project
            for project in self.projects()
            if project.is_complete
        ]

    def projects_by_category(
        self,
        category: str,
    ) -> list[DoodleProject]:
        """Return projects in a category."""
        return [
            project
            for project in self.projects()
            if project.category == category
        ]

    def project_count(self) -> int:
        """Return the number of registered projects."""
        return len(self._projects)