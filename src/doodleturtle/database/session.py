"""
Database session management for DoodleTurtleAI.
"""

from sqlalchemy.orm import sessionmaker

from doodleturtle.database.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)