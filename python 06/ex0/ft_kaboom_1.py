print("=== Kaboom 1 ===\n"
      "Access to alchemy/grimoire/dark_spellbook.py directly\n"
      "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

import alchemy.grimoire.dark_spellbook  # noqa: E402

print({alchemy.grimoire.dark_spellbook.dark_spell_record("aaa", "arsenic")})
