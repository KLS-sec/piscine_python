#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    test_transform(transform_factory)


if __name__ == "__main__":
    main()


"""
Exercice
1 lire l exercice (liste de choses à apprendre)
2 remplir le work instructions
2 Lire le w3school/autre concerne
3 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants (utiliser checklist projet)
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

si bloqué
-Exemple
-GPT
-exo mal fait de tt facon, ne pas m'épuiser dessus
-----------------------------------------------------------------
G [tutorials]
G Abstract Programming Patterns
0 abstract factory design pattern
https://realpython.com/factory-method-python/#basic-implementation-of-factory-method
2 abstract strategy pattern


[authorized functions]
builtins, standard types, import typing, import abc

[exercise instructions - to reorganize]

G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check this using mypy.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized, except for eval() and exec().
• Your functions should handle exceptions gracefully to avoid crashes.
• External libraries are forbidden.

A __init__.py file is MANDATORY for each exercise folder. All testing code
will be located at the root of the git repository.

During evaluation, you may be asked to explain the design patterns explored in
this project. Focus on understanding the concepts, not just the implementation.
"""
