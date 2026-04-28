#!/usr/bin/env python3

from ex2 import (
    FlameFactory,
    AquaFactory,
    HealingCreatureFactory,
    TransformCreatureFactory,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    CreatureFactory,
    BattleStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")

            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)

            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()


"""
3 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants (utiliser checklist projet)

si bloqué
-Exemple
-GPT
-exo mal fait de tt facon, ne pas m'épuiser dessus
-----------------------------------------------------------------
G [tutorials]
G Abstract Programming Patterns # use of ABC
0 abstract factory design pattern # use of ABC for factories
https://realpython.com/factory-method-python/#basic-implementation-of-factory-method
2 abstract strategy pattern


[authorized functions]
builtins, standard types, import typing, import abc

[exercise instructions - to reorganize]
ex2/
V   BattleStrategy abstract class
V       act abstract method
V           will be called by tournament script
V       is_valid abstract method
V           return a bool to see if the creature is suitable for the strategy

    3 concrete classes, inherit from BattleStrategy
        NormalStrategy
            any creature
            juste use the attack method
        AggressiveStrategy
            for creatures with transform capabilities
            transform -> attack -> revert
        DefensiveStrategy
            for creatures with healing capabilities
            attack -> heal

    is_valid
        return false if a strategy call an invalid creature
    act
        create the "battle" and print the returns
        if called with wrong creature
            raise a dedicated excepion with a clear message



We can finally create our tournament. The tournament.py script, located at the
root of the Git repository, will proceed as follows:
• Create various Creature factories (from ex0 and ex1).
• Create the three strategies.
• Define a single battle function that:
◦ takes a list of opponents in the tournament; each opponent is defined as a
tuple consisting of a CreatureFactory and a BattleStrategy.
◦ makes each opponent fight once all other opponents.
◦ organizes each fight using each Creature’s associated strategy.
◦ handles correctly invalid Creature-strategy tuples.

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
