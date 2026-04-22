from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    valid_list: list = light_spell_allowed_ingredients()
    valid_list.append("Error")
    for y in valid_list:
        for y in ingredients:
            if y == x:
                break
            if y == "Error":
                
