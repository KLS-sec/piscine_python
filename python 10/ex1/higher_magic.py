#!/usr/bin/env python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combinated(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combinated


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, strengh: int) -> str:
        a = base_spell(target, strengh * multiplier)
        return a
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditionnal(target: str, strengh: int) -> str:
        if condition(target, strengh):
            return spell(target, strengh)
        return "Spell fizzled"
    return conditionnal


def spell_sequence(spells: list[Callable]) -> Callable:
    def chain_caster(target: str, strengh: int) -> str:
        result = ""
        for x in spells:
            result = result + x(target, strengh) + " "
        result = result[:-1]
        return result
    return chain_caster


"""
spell_sequence(spells) - Create spell sequence:
    • Return a function that casts all spells in order
    • Each spell receives the same arguments
    • Returns a list of all spell results
"""


def main() -> None:
    pass


if __name__ == "__main__":
    main()

"""
Si bloqué:
-Voir exemples
-réexpliquer par GPT
-arrêter de se casser le crâne à voir plus compliqué
-faire morceau par morceau et implémenter
---------------------------------------------
Work instruction

G [tutorials]
https://www.w3schools.com/python/ref_func_callable.asp

[authorized functions]
callable(), Callable

[needed files]
higher_magic.py


[exercise instructions - organized + general goal + explanation by gpt]
spells
    def spell(target: str, power: int) -> str
        target - power level -> return a descriptive string

[exercise instructions - original]

The following functions must be implemented:

Implementation Requirements



#################################################
G [general project instructions]
IV.1 Python Requirements
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• Exception handling should protect the data streams from corruption.
• Use type hints for all function signatures and return types.
• Focus on demonstrating functional programming patterns clearly.
• Each exercise should be in its own file with the specified name.
• Write clean, readable code that demonstrates your understanding.

IV.2 Authorized Imports
• typing module - For advanced type hints
• When using Callable as a type hint, use collections.abc
• itertools module - For advanced iteration patterns
• Essential modules for this project functools and operator will be specified
if allowed in each exercise.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized, but eval() and exec().
• Standard library modules as needed for the exercises 7 FuncMage Master the
Ancient Arts of Functional Programming

IV.3 Forbidden
• External libraries (no pip install)
• File I/O operations (focus on in-memory processing)
• Complex algorithms (keep focus on functional patterns)
• Using eval() or exec()
• Global variables (embrace functional purity when possible)

IV.4 Output Specifications Each exercise provides terminal examples showing
the suggested output format. While the core structure must be maintained, you
may customize messages to reflect your understanding of the file operations, as
long as the essential information is preserved.

During peer-review, you may be asked to explain functional programming
concepts, demonstrate how closures work, or show how decorators transform
functions. Focus on understanding the concepts, not just the implementation.

############################
# The Higher Realm: Functions Operating on Functions
Welcome to the Higher Realm, where functions become the subjects of other
functions!
Here, you’ll learn that functions are first-class citizens—they can be passed
as arguments, returned from other functions, and stored in data structures.

Your Mission: Help the Realm’s guardian, Mage Functional, create
a spell-crafting system where functions can modify, combine, and
enhance other functions. Master the art of higher-order functions!

The Challenge
Create a file higher_magic.py that demonstrates higher-order function mastery:

Context
Every spell in your grimoire follows the same contract:
def spell(target: str, power: int) -> str
A spell takes a target and a power level and returns a description string of
what happened.

Examples:
def heal(target: str, power: int) -> str:
return f"Heal restores {target} for {power} HP"
If you need inspiration for power values or target, use data_generator.py to
get sample
data.

The following functions must be implemented: Function Signatures:
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable
def conditional_caster(condition: Callable, spell: Callable) -> Callable
def spell_sequence(spells: list[Callable]) -> Callable

Implementation Requirements
spell_combiner(spell1, spell2) - Combine two spells:
• Return a new function that calls both spells with the same arguments
• The combined spell should return a tuple of both results
• Example: combined = spell_combiner(fireball, heal)
power_amplifier(base_spell, multiplier) - Amplify spell power:
• Returns a function with the same signature as the original spell
• Returns a new spell where the power is multiplied before casting.
• Example: mega_fireball = power_amplifier(fireball, 3)
conditional_caster(condition, spell) - Cast spell conditionally:
• Returns a new spell that only casts if a condition is True.
• If condition fails, return "Spell fizzled"
• Both condition and spell receive the same arguments
spell_sequence(spells) - Create spell sequence:
• Return a function that casts all spells in order
• Each spell receives the same arguments
• Returns a list of all spell results
"""
