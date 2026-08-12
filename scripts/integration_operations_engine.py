"""
Integration test for the Operations Engine.
"""

from doodleturtle.operations import OperationsEngine


def print_projects(title: str, projects: list) -> None:
    """Print a list of projects."""
    print(title)
    print("-" * len(title))

    if not projects:
        print("None")
        print()
        return

    for project in projects:
        print(
            f"- {project.name:<20}"
            f"{project.category:<12}"
            f"{project.status}"
        )

    print()


def main() -> None:
    """Run the Operations Engine integration test."""
    operations = OperationsEngine()

    operations.create_project(
        name="DoodleTurtleAI",
        category="Software",
    )

    operations.create_project(
        name="DoodleTurtleCo",
        category="Business",
    )

    operations.create_project(
        name="Finn Storybook",
        category="Storybook",
    )

    operations.create_project(
        name="Ocean Adventure",
        category="Storybook",
    )

    operations.start_project("DoodleTurtleAI")
    operations.start_project("Finn Storybook")
    operations.complete_project("DoodleTurtleCo")

    print("# Operations Engine")
    print()

    print_projects(
        "All Projects",
        operations.projects(),
    )

    print_projects(
        "Active Projects",
        operations.active_projects(),
    )

    print_projects(
        "Planning Projects",
        operations.planning_projects(),
    )

    print_projects(
        "Completed Projects",
        operations.completed_projects(),
    )

    print_projects(
        "Storybook Projects",
        operations.projects_by_category("Storybook"),
    )

    print(f"Total Projects: {operations.project_count()}")


if __name__ == "__main__":
    main()