#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)

###########################################################


def plant_test() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_test() -> None:
    raise WaterError("Not enough water in the tank!")

###########################################################


def tester() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        plant_test()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        water_test()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    try:
        plant_test()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        water_test()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("\nAll custom error types work correctly!")


def main() -> None:
    tester()


if __name__ == "__main__":
    main()
