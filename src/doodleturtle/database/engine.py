"""
Database engine for DoodleTurtleAI.

Responsible for creating the SQLAlchemy engine and
providing the database connection.
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

# Project root (DoodleTurtleAI/)
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Database location
DATABASE_DIR = PROJECT_ROOT / "data"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "doodleturtle.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine: Engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)