from doodleturtle.banner import display_banner
from doodleturtle.config import load_config
from doodleturtle.health import system_health
from doodleturtle.logger import initialize_logger


def startup() -> None:
    """Initialize DoodleTurtleAI."""

    display_banner()

    print("Loading configuration...")
    config = load_config()
    print("✓ Configuration loaded")

    initialize_logger()

    print("Running health check...")

    if system_health():
        print("✓ System Healthy")
    else:
        print("✗ System Failed")

    print()
    print(f"Welcome to {config.app_name}.")
    print("Project Genesis has officially begun.")