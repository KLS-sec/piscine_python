#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def get_age(self):
        return (self._age)

    def get_height(self):
        return (float(self._height))

    def set_age(self, age):
        if age < 0:
            print(self._name, ":Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print("Age updated: ", self._age, " days", sep="")

    def set_height(self, height):
        if height < 0:
            print(self._name, ":Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print("Height updated: ", self._height, "cm", sep="")

    def grow(self, days) -> None:
        self._height += (days * 0.8)

    def age(self, days) -> None:
        self._age += days

    def show(self) -> None:
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._age, " days old",
              sep="")


def main() -> None:
    p1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    p1.show()
    print("")
    p1.set_height(25)
    p1.set_age(-30)
    print("")
    print("Current state: ", end="")
    p1.show()


if __name__ == "__main__":
    main()


"""
class Book:
    def get_price(self):
        return self._price

    def set_price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")


book = Book("Clean Code", "Robert C. Martin", 10.0)
price = book.get_price()
book.set_price(20.0)

• Improve your Plant class in order to protect its data from corruption
• Provide controlled ways to modify plant data: set_height(), set_age()
• Provide safe ways to access plant data: get_height(), get_age()
• Ensure plant height cannot be negative through validation
• Ensure plant age cannot be negative through validation
• Print error messages from the class when invalid values are provided,
leaving data unchanged or creating the plant with default values
• Use encapsulation: prevent your class attributes from being used
directly by using the “protected” convention (not the mangling)

"""
