#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    if any(x in ingredients.lower() for x in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
