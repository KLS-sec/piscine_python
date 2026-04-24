#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory

fire = FlameFactory()
water = AquaFactory()


def checker(factory: CreatureFactory) -> None:
    print("Testing factory")
    lab_rat = factory.create_base()
    big_lab_rat = factory.create_evolved()

    print(lab_rat.describe())
    print(lab_rat.attack())
    print(big_lab_rat.describe())
    print(big_lab_rat.attack())


def battlground(aqua: CreatureFactory, fire: CreatureFactory) -> None:
    print("Testing battle")
    fire_rat = fire.create_base()
    aqua_rat = aqua.create_base()

    print(fire_rat.describe())
    print(" vs")
    print(aqua_rat.describe())
    print(" fight!")
    print(fire_rat.attack())
    print(aqua_rat.attack())


def main() -> None:
    fire = FlameFactory()
    water = AquaFactory()
    checker(fire)
    print("")
    checker(water)
    print("")
    battlground(water, fire)


if __name__ == "__main__":
    main()
"""
multicheck
tout bon
"""

"""
battle.py
    -at the root of the repository
    -use the ex0 package
    scenario:
        -instanciate(create) Flameling and Aquabub factories
        -one function check that the factoriy object received can
            -create the base and evolved creature
            -both can be described and can attack
        -another function
            -receive both factories
            -make the base creatures fight (print description/attack)
"""

"""
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

WORK INSTRUCTIONS
[authorized functions]
builtins, standard types, import typing, import abc

[exercise instructions - to reorganize]
ex0/ folder

V Creature abstract class:
    -atribute name
    -atribute type
    -abstract method attack()
    -concrete(usable) generic(type: any) method describe()
        return generic message with name and type of the creature

V concrete classes:
    -inherit from Creature class
    -Flameling, Pyrodon, Aquabub, Torragon
    -overide attack to return a string message(see exemple)

V abstract class CreatureFactory
    -create_base and create_evolved abstract method

V concrete classes:
    -inherit from CreatureFactory
    -FlameFactory, AquaFactory
    -handle the creation of base and evolved creatures

V __init__.py
    -only expose factories


battle.py
    -at the root of the repository
    -use the ex0 package
    scenario:
        -instanciate(create) Flameling and Aquabub factories(?)
        -one function check that the factoriy object received can
            -create the base and evolved creature
            -both can be described and can attack
        -another function
            -receive both factories
            -make the base creatures fight (print description/attack)

--------

The battle.py script, at the root of the repository, will test the ex0 package.
The following scenario will be implemented:
• Instantiate the Flameling and Aquabub factories.
• Use a single function that receives a factory object and verifies that it
can create the base and evolved Creature, and then each Creature can be
described and can attack.
• Another function that receives both factories and makes base Creature fight.

You can use different Creatures, but you must keep the involved
concepts (families and abstract factories).

--------
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

#############################
focus on the abstract factory design pattern. You will implement the following
elements in the ex0/ folder:

• A Creature abstract class that holds attributes for the name and the type of
the Creature, an abstract method attack and a concrete generic method describe
that will return a standard message using the name and the type of the
Creature.
• The following concrete classes that inherit from Creature: Flameling,
Pyrodon, Aquabub, and Torragon. Their attack method will return an appropriate
string message (see example).
• A CreatureFactory abstract class that will allow you to create the base
Creature and the evolved Creature for the same family, using the create_base
and create_evolved abstract methods.
• The concrete classes FlameFactory and AquaFactory, inheriting from
CreatureFactory, that will handle the creation of the base and evolved Creature
for each family (respectively Flameling and Pyrodon for FlameFactory, and
Aquabub and Torragon for AquaFactory).
• Your ex0 package cannot expose concrete Creature directly, it must only
expose factories.

The battle.py script, at the root of the repository, will test the ex0 package.
The following scenario will be implemented:
• Instantiate the Flameling and Aquabub factories.
• Use a single function that receives a factory object and verifies that it
can create the base and evolved Creature, and then each Creature can be
described and can attack.
• Another function that receives both factories and makes base Creature fight.
You can use different Creatures, but you must keep the involved
concepts (families and abstract factories).

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
#############################

ex0: Abstract Factory pattern
    Creature (ABC) → attack() abstract, describe() concrete
    Concrete creatures (Flameling, Pyrodon, Aquabub, Torragon)
    CreatureFactory (ABC) → create_base(), create_evolved()
    Concrete factories: FlameFactory, AquaFactory
    Package must expose only factories
ex1: Capabilities via multiple inheritance
    HealCapability, TransformCapability (independent ABCs)
    New creatures combining Creature + Capability
    Factories: HealingCreatureFactory, TransformCreatureFactory
    Behavior affects attack()
    Still only factories exposed
ex2: Strategy pattern
    BattleStrategy (ABC): act(), is_valid()
    Strategies:
        NormalStrategy
        AggressiveStrategy (transform required)
        DefensiveStrategy (heal required)
    Validation + exception handling required
    Tournament orchestrates interactions
"""
