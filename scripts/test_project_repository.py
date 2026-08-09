"""
Integration test for the ProjectRepository.

This script creates the first Project in the Turtle Brain.
"""

from doodleturtle.database.models.project import Project
from doodleturtle.database.session import SessionLocal
from doodleturtle.repositories.project_repository import ProjectRepository


def main() -> None:
    """Create and retrieve Projects from the Turtle Brain."""

    session = SessionLocal()

    try:
        repository = ProjectRepository(session)

        project = Project(
            name="Project Genesis",
            description="Creation of the DoodleTurtleAI operating system.",
            status="ACTIVE",
        )

        repository.create(project)

        projects = repository.get_all()

        print()
        print("========================================")
        print("Turtle Brain Memories")
        print("========================================")

        for project in projects:
            print(f"ID: {project.id}")
            print(f"Name: {project.name}")
            print(f"Status: {project.status}")
            print("----------------------------------------")

        print(f"Total Projects: {len(projects)}")
        print("========================================")

    finally:
        session.close()


if __name__ == "__main__":
    main()