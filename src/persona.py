"""
Persona module.
"""

from dataclasses import dataclass


@dataclass
class Persona:
    name: str
    bio: str
    key_goals: list[str]
    primary_frustrations: list[str]
    generation_input: str
