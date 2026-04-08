#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return float(self._height)

    def set_age(self, age) -> None:
        if age < 0:
            print(self._name, ":Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print("Age updated: ", self._age, " days", sep="")

    def set_height(self, height) -> None:
        if height < 0:
            print(self._name, ":Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print("Height updated: ", self._height, "cm", sep="")

    def grow(self, days) -> None:
        self._height += (days * 0.8)

    def age(self, days) -> None:
        self._age += days

    def show(self) -> None:
        print(self._name, ": ", self.get_height(), "cm, ",
              self.get_age(), " days old",
              sep="")


def main() -> None:
    p1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    p1.show()
    print("")
    p1.set_height(25)
    p1.set_age(30)
    print("")
    p1.set_height(-25)
    p1.set_age(-30)
    print("")
    print("Current state: ", end="")
    p1.show()


if __name__ == "__main__":
    main()
