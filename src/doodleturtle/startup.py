from doodleturtle.banner import display_banner
from doodleturtle.config import load_config
from doodleturtle.database.init_db import initialize_database
from doodleturtle.health import system_health
from doodleturtle.knowledge import initialize_knowledge
from doodleturtle.logger import initialize_logger


def startup() -> None:
    """Initialize DoodleTurtleAI."""

    display_banner()

    print("Loading configuration...")
    config = load_config()
    print("✓ Configuration loaded")

    initialize_logger()

    print("Initializing Turtle Brain...")
    initialize_database()
    print("✓ Turtle Brain Ready")

    print("Initializing Knowledge Library...")
    initialize_knowledge()
    print("✓ Knowledge Library Ready")

    print("Running health check...")

    if system_health():
        print("✓ System Healthy")
    else:
        print("✗ System Failed")

    print()
    print(f"Welcome to {config.app_name}.")
    print("Project Genesis has officially begun.")