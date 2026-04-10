#!/usr/bin/env python3

from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    while True:

        u_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = u_input.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(coordinates[0].strip())
            y = float(coordinates[1].strip())
            z = float(coordinates[2].strip())
            return (x, y, z)
        except ValueError as e:
            invalid_value = str(e).split("'")[1]
            print(f"Error on parameter '{invalid_value}': {e}")


def distance(t1: tuple[float, float, float],
             t2: tuple[float, float, float]) -> float:
    result = sqrt(
        (t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2 + (t2[2] - t1[2]) ** 2)
    return result


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    set_one = get_player_pos()

    print(f"Got a first tuple: {set_one}")
    print(f"It includes: X={set_one[0]}, Y={set_one[1]}, Z={set_one[2]}")

    center = (0.0, 2.5 - 2.5, 0.0)
    dist_center = distance(set_one, center)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    set_two = get_player_pos()

    dist_sets = distance(set_one, set_two)
    print(f"Distance between the 2 sets of coordinates: {round(dist_sets, 4)}")


if __name__ == "__main__":
    main()
