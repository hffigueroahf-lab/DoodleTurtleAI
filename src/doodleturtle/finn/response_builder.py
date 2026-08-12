"""
Finn Response Builder.

Transforms intelligence responses into
Finn's educational voice.
"""

from doodleturtle.intelligence.response import IntelligenceResponse


class FinnResponseBuilder:
    """Build child-friendly responses."""

    def build(
        self,
        response: IntelligenceResponse,
    ) -> str:
        """Build a response for children."""
        return (
            "That's a wonderful question!\n\n"
            "Let's explore it together.\n\n"
            "I'm using everything I've learned "
            "to help answer your question.\n\n"
            "----\n\n"
            f"{response.content}\n\n"
            "----\n\n"
            "Keep asking questions.\n"
            "Curiosity helps us discover amazing things!"
        )