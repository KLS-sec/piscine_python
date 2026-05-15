#!/usr/bin/env python3

import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting{func.__name__}...")
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print(f"Spell completed in {e - s:.3f} seconds")
        return result
    return wrapper


"""
spell_timer(func) - Time execution decorator:
Create a decorator that measures function execution time
• Print "Casting function_name..." before execution
• Print "Spell completed in X.XXX seconds" after execution (3 decimal places)
• Use functools.wraps to preserve original function metadata
• Return the original function’s result

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper
"""


def power_validator(min_power: int) -> Callable[[Callable[..., str]],
                                                Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @functools.wraps(func)
        def wrapper(self: Any, spell_name: str, power: int) -> Any:
            if power >= min_power:
                return func(self, spell_name, power)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


"""
power_validator(min_power) - Parameterized validation decorator:
Create a decorator factory that validates power levels
• Applied on a standalone function whose first argument is power.
• If power is valid (>= min_power), execute the function normally
• If invalid, return "Insufficient power for this spell"
• Use functools.wraps properly

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator
"""


def retry_spell(max_attempts: int) -> Callable[
     [Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            x = 0
            while x < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    x += 1
                    if x < max_attempts:
                        print("Spell failed, retrying... (attempt"
                              f" {x}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


"""
retry_spell(max_attempts) - Retry decorator:
Create a decorator that retries failed spells
• If function raises an exception, retry up to max_attempts times
• Print "Spell failed, retrying... (attempt n/max_attempts)"
• If all attempts fail:
return "Spell casting failed after max_attempts attempts"
• If one attempt succeeds, return its result normally

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt"
                            " {x}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator
"""


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


"""
MageGuild class - Demonstrate staticmethod:
• validate_mage_name(name) - Static method that checks if name is valid
• Name is valid if it’s at least 3 characters and contains only letters/spaces
• cast_spell(self, spell_name, power) - Instance method
• Should use the power_validator decorator with min_power=10
• When power is valid, return "Successfully cast spell_name with <power> power"
• Otherwise return "Insufficient power for this spell"

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

"""


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.1)
        return f"Fireball cast on {target}"

    result = fireball("dragon")
    print("Result:", result)
    print()

    print("Testing retry spell...")

    import random

    @retry_spell(3)
    def unstable_spell() -> str:
        if random.random() < 0.7:
            raise ValueError("fail")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print()

    print("Testing MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()

"""
Exercice
1 lire l exercice, lister les choses à apprendre
2 remplir le work instructions
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
https://www.geeksforgeeks.org/python/python-functools-wraps-function/

[authorized functions]
functools.wraps, staticmethod

[needed files]
decorator_mastery.py

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]


####################################################

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
may customize messages to reflect your understanding of the file operations,
as long as the essential information is preserved.

During peer-review, you may be asked to explain functional programming
concepts, demonstrate how closures work, or show how decorators transform
functions. Focus on understanding the concepts, not just the implementation.




##############################################

import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    if attempt < max_attempts:
                        print("Spell failed, retrying... (attempt"
                              f" {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.1)
        return f"Fireball cast on {target}"

    result = fireball("dragon")
    print("Result:", result)
    print()

    print("Testing retry spell...")

    import random

    @retry_spell(3)
    def unstable_spell() -> str:
        if random.random() < 0.7:
            raise ValueError("fail")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print()

    print("Testing MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
"""
