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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_a: str, plant_b: str, plant_c: str) -> None:
    print("Opening watering system")
    try:
        water_plant(plant_a)
        water_plant(plant_b)
        water_plant(plant_c)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

###########################################################


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "lettuce", "Carrots")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
