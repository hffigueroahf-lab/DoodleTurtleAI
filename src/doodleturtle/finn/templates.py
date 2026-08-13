"""
Finn Educational Templates.

Reusable educational templates for building
learning experiences.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EducationalTemplate:
    """Represent an educational experience template."""

    name: str
    fun_fact_prefix: str
    activity_prefix: str
    reflection_prefix: str


NATURE_TEMPLATE = EducationalTemplate(
    name="Nature",
    fun_fact_prefix="🌿 Did you know?",
    activity_prefix="🎨 Nature Activity",
    reflection_prefix="🤔 Think About Nature",
)


SCIENCE_TEMPLATE = EducationalTemplate(
    name="Science",
    fun_fact_prefix="🔬 Science Fact",
    activity_prefix="🧪 Try This",
    reflection_prefix="💡 Think Like a Scientist",
)


CREATIVITY_TEMPLATE = EducationalTemplate(
    name="Creativity",
    fun_fact_prefix="🎨 Creative Idea",
    activity_prefix="✏️ Create Something",
    reflection_prefix="✨ Imagine This",
)