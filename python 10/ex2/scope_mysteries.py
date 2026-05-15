#!/usr/bin/env python3

from typing import Any
from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    x = 0

    def counter() -> int:
        nonlocal x
        x = x + 1
        return x
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    x = initial_power

    def battery(charge: int) -> int:
        nonlocal x
        x = x + charge
        return x
    return battery


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    x = enchantment_type

    def booster(target: str) -> str:
        nonlocal x
        x = x
        y = x + " " + target
        return y
    return booster


def memory_vault() -> dict[str, Callable[..., Any]]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        try:
            return memories.get(key, "Memory not found")
        except Exception:
            return "Memory not found"

    return {"store": store, "recall": recall, }


def main() -> None:
    print("Testing mage counter...")
    counter_one = mage_counter()
    for a in range(3):
        print(counter_one(), end="")
        a = a
    print("")
    counter_two = mage_counter()
    for a in range(4):
        print(counter_two(), end="")
        a = a
    print("")

    print("\nTesting spell accumulator...")
    battery = spell_accumulator(5)
    print("Base = 5")
    print("5 + 3 =", battery(3))
    print("+ 4 =", battery(4))
    print("")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("flaming")
    print(flaming("sword"))
    flaming = enchantment_factory("frost")
    print(flaming("shield"))
    print("")

    print("Testing memory vault...")
    storage = memory_vault()
    storage["store"]("secret1", 1)
    storage["store"]("secret2", 2)

    print(storage["recall"]("secret1"))
    print(storage["recall"]("secret2"))
    try:
        print(storage["error"]("secret2"))
    except Exception:
        print("Memory not found")


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
https://www.w3schools.com/python/ref_keyword_nonlocal.asp

[authorized functions]
nonlocal

[Tools]

[needed files]

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]
def memory_vault() -> dict[str, Callable]

memory_vault() - Create a memory management system:
• Return a dict with ’store’ and ’recall’ functions
• ’store’ function: takes (key, value) and stores the memory
• ’recall’ function: takes (key) and returns stored value or "Memory not found"
• Use closure to maintain private memory storage

###################################
def mage_counter() -> Callable
def spell_accumulator(initial_power: int) -> Callable
def enchantment_factory(enchantment_type: str) -> Callable
def memory_vault() -> dict[str, Callable]

Implementation Requirements
mage_counter() - Create a counting closure:
• Return a function that counts how many times it’s been called
• Each call should return the current count (starting from 1)
• The counter should persist between calls
• Creating two separate counters must yield independent state.
• Use closure to maintain state without global variables
spell_accumulator(initial_power) - Create power accumulator:
• Return a function that accumulates power over time
• Each call adds the given amount to the total power
• Return the new total power after each addition
• Start with initial_power as the base
enchantment_factory(enchantment_type) - Create enchantment functions:
• Return a function that applies the specified enchantment
• The returned function takes an item name and returns enchanted description
• Format: "enchantment_type item_name" (e.g., "Flaming Sword")
• Each factory creates functions with different enchantment types
memory_vault() - Create a memory management system:
• Return a dict with ’store’ and ’recall’ functions
• ’store’ function: takes (key, value) and stores the memory
• ’recall’ function: takes (key) and returns stored value or "Memory not found"
• Use closure to maintain private memory storage


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
