from .Factories import FlameFactory, AquaFactory, CreatureFactory

__all__ = ["FlameFactory", "AquaFactory", "CreatureFactory"]

"""
__init__.py
    -only expose factories


Your ex0 package must behave like this:

External code (battle.py) is allowed to import and use:
FlameFactory
AquaFactory
CreatureFactory (abstract type if needed for typing)

External code is NOT allowed to access:
Flameling
Pyrodon
Aquabub
Torragon
or any other concrete Creature class
"""
