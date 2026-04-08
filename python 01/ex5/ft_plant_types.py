#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def get_age(self) -> int:
        return (self._age)

    def get_height(self) -> float:
        return (float(self._height))

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
            self._height = float(height)
            print("Height updated: ", self._height, "cm", sep="")

    def grow(self, days) -> None:
        self._height += (days * 2.1)

    def age(self, days) -> None:
        self._age += days

    def show(self) -> None:
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._age, " days old",
              sep="")

#####################################


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self, bin) -> None:
        if bin:
            print("", self._name, "is blooming beautifully!")
        else:
            print("", self._name, "has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(" Color:", self._color)


#####################################


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)

    def produce_shade(self, shader) -> None:
        if shader:
            print("Tree ", self._name, " now produces a shade of ",
                  self._height, "cm long and ", self._trunk_diameter,
                  "cm wide.", sep="")

    def show(self) -> None:
        super().show()
        print(" Trunk diameter: ", self._trunk_diameter, "cm long", sep="")

#####################################


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, _days) -> None:
        super().age(_days)
        self._nutritional_value += _days

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self._harvest_season)
        print(" Nutritional value:", self._nutritional_value)

#####################################


def main() -> None:
    print("=== Garden Plant Types ===")
    F = Flower("Rose", 15, 10, "red")
    T = Tree("Oak", 200, 365, 5)
    V = Vegetable("Tomato", 5, 10, "April", 0)
    print("\n===", F.__class__.__name__)
    F.show()
    F.bloom(False)
    print("[asking the rose to bloom]")
    F.show()
    F.bloom(True)
    print("\n===", T.__class__.__name__)
    T.show()
    T.produce_shade(False)
    print("[asking the oak to produce shade]")
    T.produce_shade(True)
    print("\n===", V.__class__.__name__)
    V.show()
    print("[make tomato grow and age for 20 days]")
    V.age(20)
    V.grow(20)
    V.show()


if __name__ == "__main__":
    main()
