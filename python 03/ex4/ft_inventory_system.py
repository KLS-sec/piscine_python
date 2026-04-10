#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, qtty = arg.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(qtty)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory[name] = quantity

    if len(inventory) > 0:
        total = sum(inventory.values())
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)} items: {total}")

        for item in inventory:
            if total > 0:
                print(f"Item {item} represents"
                      f" {round(inventory[item] / total * 100, 1)}%")
            else:
                print(f"Item {item} represents 0%")

        items = list(inventory.keys())
        max_val = items[0]
        min_val = items[0]

        for item in items:
            if inventory[item] > inventory[max_val]:
                max_val = item
            if inventory[item] < inventory[min_val]:
                min_val = item
        print(f"Item most abundant: {max_val} with quantity"
              f" {inventory[max_val]}")
        print(f"Item least abundant: {min_val} with quantity"
              f" {inventory[min_val]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

"""
sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
"""
