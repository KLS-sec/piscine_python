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


def partial_enchanter(
        base_enchantment: Callable[..., str]) -> dict[str, Callable[..., str]]:
    returner: dict[str, Callable[..., str]] = {}
    a = functools.partial(base_enchantment, 50, "fire")
    b = functools.partial(base_enchantment, 50, "water")
    c = functools.partial(base_enchantment, 50, "light")
    returner["0"] = a
    returner["1"] = b
    returner["2"] = c
    return returner


@lru_cache(maxsize=50)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"damages {spell * 2}"

    @dispatcher.register
    def _(spell: str) -> str:
        return "super" + spell

    @dispatcher.register
    def _(spell: list[Any]) -> str:
        return (f"Cast {len(spell)} spells")

    return dispatcher


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

    print("\nTesting spell_dispatcher")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(3.14))


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
https://www.w3schools.com/python/ref_module_functools.asp
https://www.geeksforgeeks.org/python/reduce-in-python/
https://www.geeksforgeeks.org/python/partial-functions-python/
https://www.geeksforgeeks.org/python/function-overloading-with-singledispatch-functools/

[authorized functions]

[Tools]

[needed files]

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]

G [general project instructions]
• typing module - For advanced type hints
• When using Callable as a type hint, use collections.abc
• itertools module - For advanced iteration patterns
• Essential modules for this project functools and operator will be
specified if allowed in each exercise.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized, but eval() and exec().
• Standard library modules as needed for the exercises

IV.4 Output Specifications Each exercise provides terminal examples
showing the suggested output format. While the core structure must be
maintained, you may customize messages to reflect your understanding of
the file operations, as long as the essential information is preserved.

During peer-review, you may be asked to explain functional programming
concepts, demonstrate how closures work, or show how decorators transform
functions. Focus on understanding the concepts, not just the
implementation.

"""
