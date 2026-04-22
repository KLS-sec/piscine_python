import alchemy.grimoire as biblio

# init grimoire

print("=== Kaboom 0 ===\n"
      "Using grimoire module directly\n"
      "Testing record light spell: ",
      biblio.light_spellbook.light_spell_record(
        "Fantasy",
        "Earth, wind and fire"))

"""
def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({result})"
"""
