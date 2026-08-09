"""
Database initialization for DoodleTurtleAI.
"""

from doodleturtle.database.base import Base
from doodleturtle.database.engine import engine

# Import all models here so SQLAlchemy registers them.
from doodleturtle.database.models import project  # noqa: F401


def initialize_database() -> None:
    """Create all database tables."""

    Base.metadata.create_all(bind=engine)