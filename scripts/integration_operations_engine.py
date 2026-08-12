"""
Integration test for the Operations Engine.
"""

from doodleturtle.operations import OperationsEngine
from doodleturtle.operations.project import DoodleProject


def main() -> None:
    """Run the Operations Engine integration test."""
    operations = OperationsEngine()

    operations.add_project(
        DoodleProject(
            name="DoodleTurtleAI",
            category="Software",
        )
    )

    operations.add_project(
        DoodleProject(
            name="DoodleTurtleCo",
            category="Business",
        )
    )

    operations.add_project(
        DoodleProject(
            name="Finn Storybook",
            category="Storybook",
        )
    )

    print("# Operations Engine")
    print()

    print("Registered Projects")
    print("-------------------")

    for project in operations.projects():
        print(
            f"- {project.name} "
            f"({project.category}) "
            f"[{project.status}]"
        )

    print()
    print(f"Total Projects: {operations.project_count()}")


if __name__ == "__main__":
    main()