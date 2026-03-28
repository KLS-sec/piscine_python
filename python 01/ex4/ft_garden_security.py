#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: float, age: int):
            self._name = name
            self._height = height
            self._age = age

        def get_name(self):
            return self._name

        def get_height(self):
            return self._height

        def set_height(self, updated_height):
            if updated_height >= 0:
                self._height = updated_height
                print("Height updated:", self._height, "cm")

            else:
                print(self._name, ": Error, height can't be negative", sep="")
                print("Height update rejected")

        def get_age(self):
            return self._age

        def set_age(self, update_age):
            if update_age >= 0:
                self._age = update_age
                print("Age updated:", self._age, "days")
            else:
                print(self._name, ": Error, age can't be negative", sep="")
                print("Age update rejected")

        def show(self, time: int):
            self.time = time
            print(self._name, ": ", self.get_height(), "cm, ", self.get_age(),
                  " days old", sep="")

    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    p1.show(0)
    print("")
    p1.set_height(-25)
    p1.set_age(30)
    print("")
    print("Current state: ", end="")
    p1.show(0)


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
