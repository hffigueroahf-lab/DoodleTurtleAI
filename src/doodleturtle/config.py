from dataclasses import dataclass


@dataclass
class AppConfig:
    app_name: str = "DoodleTurtleAI"
    version: str = "0.0.1-alpha"


def load_config() -> AppConfig:
    return AppConfig()