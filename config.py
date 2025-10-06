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
    
    return _

GOOGLE_API_KEY = _confirm_existence_and_get_from_env("GOOGLE_API_KEY")
DEMOGRAPHIC_GENERATOR_LLM = getenv("DEMOGRAPHIC_GENERATOR_LLM", "gemini-2.5-flash")
