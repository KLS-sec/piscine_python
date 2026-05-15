#!/usr/bin/env python3

from operator import add
from operator import mul

from typing import Any

from collections.abc import Callable

import functools
from functools import lru_cache


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return functools.reduce(add, spells)

    if operation == "max":
        return functools.reduce(max, spells)

    if operation == "min":
        return functools.reduce(min, spells)

    if operation == "multiply":
        return functools.reduce(mul, spells)

    raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    returner = {}
    returner["0"] = functools.partial(base_enchantment, 50, "fire")
    returner["1"] = functools.partial(base_enchantment, 50, "water")
    returner["2"] = functools.partial(base_enchantment, 50, "light")
    return returner


@lru_cache(maxsize=50)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    pass


"""
You can verify caching works via memoized_fibonacci.cache_info().
spell_dispatcher() - Create single dispatch system:
• Use decorator functools.singledispatch to create a spell system
• The base function receives Any and handles unknown spell type
• Handle different types: int (damage spell), str (enchantment),
list (multi-cast)
• Return the dispatcher function
• Each type should have appropriate spell behavior

def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher

    main
    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(3.14))
"""


def main() -> None:

    print("Test spell reducer")
    operations = [1, 2, 3, 4]
    addition = spell_reducer(operations, "add")
    maximum = spell_reducer(operations, "max")
    minimum = spell_reducer(operations, "min")
    multiplication = spell_reducer(operations, "multiply")
    print(addition)
    print(maximum)
    print(minimum)
    print(multiplication)
    try:
        spell_reducer(operations, "x")
    except ValueError as e:
        print(e)

    print("\nTest partial_enchanter")

    def blast(power: int, element: str, target: str) -> str:
        return (f"{element} blast, {power} damages on {target}")
    blaster = partial_enchanter(blast)
    for x in blaster:
        print(blaster[x]("dragon"))

    print("\nTest lru_cache")
    print(memoized_fibonacci(6))
    print(memoized_fibonacci(8))
    print(memoized_fibonacci(10))


if __name__ == "__main__":
    main()

"""
Exercice
3 Lire le w3school/autre concerne
4 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

Si bloqué:
-Voir exemples
-réexpliquer par GPT
-arrêter de se casser le crâne à voir plus compliqué
-faire morceau par morceau et implémenter
---------------------------------------------
Work instruction

G [tutorials]
https://www.w3schools.com/python/ref_module_functools.asp
https://www.geeksforgeeks.org/python/reduce-in-python/
https://www.geeksforgeeks.org/python/partial-functions-python/

[authorized functions]

[Tools]

[needed files]

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]

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
• Essential modules for this project functools and operator will be
specified if allowed in each exercise.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized, but eval() and exec().
• Standard library modules as needed for the exercises 7 FuncMage Master
the Ancient Arts of Functional Programming

IV.3 Forbidden
• External libraries (no pip install)
• File I/O operations (focus on in-memory processing)
• Complex algorithms (keep focus on functional patterns)
• Using eval() or exec()
• Global variables (embrace functional purity when possible)

IV.4 Output Specifications Each exercise provides terminal examples
showing the suggested output format. While the core structure must be
maintained, you may customize messages to reflect your understanding of
the file operations, as long as the essential information is preserved.

During peer-review, you may be asked to explain functional programming
concepts, demonstrate how closures work, or show how decorators transform
functions. Focus on understanding the concepts, not just the
implementation.

"""
