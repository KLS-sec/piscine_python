from ex0.elements import create_fire, create_water
from elements import create_air, create_earth


def healing_potion() -> str:
    print(f"Healing potion brewed with '{create_earth()}' and "
          f"'{create_air()}'")


def strengh_potion() -> str:
    print(f"Healing potion brewed with ’{create_earth()}’ and ’{create_water()}")


__all__ = ["create_fire"]  # because of create_fire
