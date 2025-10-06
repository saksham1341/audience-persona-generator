"""
Configuration module.
"""

from os import getenv

def _confirm_existence_and_get_from_env(variable_name) -> str:
    """
    Confirm the existence of a variable in the environment and retrieve it's value.
    """
    
    _ = getenv(variable_name, None)
    if _ is None:
        raise RuntimeError(f"`{variable_name}` not found in the environment.")

GEMINI_API_KEY = _confirm_existence_and_get_from_env("GEMINI_API_KEY")
