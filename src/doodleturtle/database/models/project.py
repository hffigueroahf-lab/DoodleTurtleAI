"""
Project model for DoodleTurtleAI.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from doodleturtle.database.base import Base
from doodleturtle.database.models.model_base import TimestampMixin


class Project(Base, TimestampMixin):
    """Represents a business project."""

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Planning",
    )