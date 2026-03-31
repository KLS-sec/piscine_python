#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
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
    print("=== Garden Plant Growth ===")

    p1 = Plant("Rose", 25.0, 30)

    for n in range(1, 8):
        print("=== Day", n, "===")
        p1.show()
        p1.grow(1)
        p1.age(1)

    print("Growth this week:", round((n - 1) * 0.8, 2), "cm")


if __name__ == "__main__":
    main()
