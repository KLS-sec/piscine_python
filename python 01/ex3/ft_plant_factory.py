#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def grow(self, days) -> None:
        self._height += (days * 0.8)

    def age(self, days) -> None:
        self._age += days

    def show(self) -> None:
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._age, " days old",
              sep="")


def main() -> None:
    plants = [  # List
        Plant("Rose", 25, 30),  # Instance / object
        Plant("Oak", 200, 365),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Fern", 15, 120)
    ]

    for p in plants:
        print("Created: ", end="")
        p.show()


if __name__ == "__main__":
    main()
