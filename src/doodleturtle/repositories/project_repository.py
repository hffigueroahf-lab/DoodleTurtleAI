"""
Project repository for DoodleTurtleAI.

Responsible for all Project data operations.
"""

from sqlalchemy.orm import Session

from doodleturtle.database.models.project import Project


class ProjectRepository:
    """Repository for Project records."""

    def __init__(self, session: Session):
        """Initialize the repository with a database session."""
        self.session = session

    def create(self, project: Project) -> Project:
        """Store a Project in the Turtle Brain."""

        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)

        return project
    def get_all(self) -> list[Project]:
        """Return all Projects from the Turtle Brain."""

        return self.session.query(Project).all()