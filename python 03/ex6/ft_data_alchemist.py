#!/usr/bin/env python3

import random


def capitalize_entry(names: list[str]) -> list[str]:  # B
    return [x.capitalize() for x in names]
    """capitalized = []
    for x in names:
        capitalized.append(x.capitalize())
    return (capitalized)"""


def capital_entry(names: list[str]) -> list[str]:  # B
    return [x for x in names if x == x.capitalize()]


def dict_maker(capitalized: list[str]) -> dict[str, int]:  # C
    return {x: random.randint(0, 1000) for x in capitalized}


def a_average(scores: dict[str, int], average: float) -> dict[str, int]:  # E
    return {x: scores[x] for x in scores if scores[x] > average}
    """a_a_scores = dict()
    print(type(scores))
    for x in scores:
        i = scores[x]
        if i > average:
            a_a_scores[x] = scores[x]
    return (a_a_scores)"""

#############################################


def main() -> None:
    # A
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
             'kevin', 'Liam']
    # B
    capitalized = capitalize_entry(names)
    good_entry: list[str] = capital_entry(names)
    # C
    scores: dict[str, int] = dict_maker(capitalized)

    # D
    average: float = 0
    for x in scores:
        average += scores[x]
    average = round(average / len(scores), 1)

    # E
    a_a_scores = a_average(scores, average)

    # F
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {good_entry}\n")
    print(f"Score dict: {scores}")
    print(f"Score average is {average}")
    print(f"High scores: {a_a_scores}")


if __name__ == "__main__":
    main()
