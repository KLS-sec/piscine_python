#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: float, age: int) -> None:
            self._name = name
            self._height = height
            self._age = age

        def get_name(self) -> str:
            return self._name

        def get_height(self) -> int:
            return self._height

        def set_height(self, updated_height: int) -> None:
            if updated_height >= 0:
                self._height = updated_height
                print("Height updated:", self._height, "cm")

            else:
                print(self._name, ": Error, height can't be negative", sep="")
                print("Height update rejected")

        def get_age(self) -> int:
            return self._age

        def set_age(self, update_age: int) -> None:
            if update_age >= 0:
                self._age = update_age
                print("Age updated:", self._age, "days")
            else:
                print(self._name, ": Error, age can't be negative", sep="")
                print("Age update rejected")

        def show(self, time: int) -> None:
            self.time = time
            print(self._name, ": ", self.get_height(), "cm, ", self.get_age(),
                  " days old", sep="")

###########################

    class Flower(Plant):
        def __init__(self, name: str, height: float, age: int, color: str) -> None:
            super().__init__(name, height, age)
            self._color = color

        def get_color():
            return
        
        def set_color():
            return

        def bloom(self):
            return (0)

        def show(self, time: int):
            self.time = time
            print(self._name, ": ", self.get_height(), "cm, ", self.get_age(),
                  " days old", sep="")
            print(" Color: ", self._color, sep="")

###########################

    class Tree(Plant):
        def __init__(self, name: str, height: float, age: int,
                     trunk_diameter: int):
            super().__init__(name, height, age)
            self._trunk_diameter = trunk_diameter

        def shade(self):
            return (0)

###########################

    class Vegetable(Plant):
        def __init__(self, name: str, height: float, age: int,
                     harvest_season: str, nutritional_value: int):
            super().__init__(name, height, age)
            self._harvest_season = harvest_season
            self.nutritional_value = nutritional_value

    print("=== Garden Security System ===")
    p1 = Flower("Rose", 15, 10, "red")
    print("Plant created: ", end="")
    p1.show(0)
    print("")
    p1.set_height(-25)
    p1.set_age(-30)
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

Requirements:
• Start with your Plant class from the previous exercise, which holds the
common features (name, height, and age)
• Create specialized types: Flower, Tree, and Vegetable
• Each specialized type should inherit the basic plant features
• Flower needs: a color attribute and ability to bloom()
• Tree needs: a trunk_diameter attribute and the ability to produce_shade()
• Vegetable needs: a harvest_season and a nutritional_value attributes
• When creating specialized plants, call the parent methods from inside your
new class using super(). It can be applied to any method, including __init__()
• A call to show() on a specialized class needs to print the standard Plant
output and the extra characteristics of your specialized plant. Your method
override can re-use the already existing code in the parent.
• Create at least one instance of each plant type; make the flower bloom; make
the nutritional value start from 0, then increase when the vegetable’s age()
and grow() methods are called.
17
Code Cultivation Object-Oriented Garden Systems
• Avoid duplicating common plant code across different specialized types.
• No need to validate the new attributes in the three new classes.
"""
