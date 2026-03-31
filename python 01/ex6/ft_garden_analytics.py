#!/usr/bin/env python3

class Plant:
    class _Stats:  # nested class (internal use)
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self):
            print(f"Stats: {self.get_grow_calls()} grow, "
                  f"{self.get_age_calls()} "
                  f"age, {self.get_show_calls()} show")

        def called_grow(self) -> None:
            self._grow_calls += 1

        def called_age(self) -> None:
            self._age_calls += 1

        def called_show(self) -> None:
            self._show_calls += 1

        def get_grow_calls(self) -> int:
            return (self._grow_calls)

        def get_age_calls(self) -> int:
            return (self._age_calls)

        def get_show_calls(self) -> int:
            return (self._show_calls)

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age
        self._stats = Plant._Stats()

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
        self._stats.called_grow()

    def age(self, days) -> None:
        self._age += days
        self._stats.called_age()

    def show(self) -> None:
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._age, " days old",
              sep="")
        self._stats.called_show()

    @staticmethod
    def age_check(value):
        print("Is", value, "days more than a year? -> ", end="")
        if value > 365:
            print("True")
        else:
            print("False")
#####################################


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = bool(0)

    def bloom(self, bin: bool):
        self._blooming = bin

    def show(self) -> None:
        super().show()
        print(" Color:", self._color)
        if self._blooming:
            print("", self._name, "is blooming beautifully!")
        else:
            print("", self._name, "has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seed_number = 0

    def bloom(self, bin: bool):
        super().bloom(bin)
        self._seed_number = 42

    def show(self) -> None:
        super().show()
        print(" Seeds:", self._seed_number)
#####################################


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._shade_call = 0

    def produce_shade(self, shader) -> None:
        if shader:
            print("Tree ", self._name, " now produces a shade of ",
                  self._height, "cm long and ", self._trunk_diameter,
                  "cm wide.", sep="")
        self._shade_call += 1

    def show(self) -> None:
        super().show()
        print(" Trunk diameter: ", self._trunk_diameter, "cm long", sep="")

    def display(self) -> None:
        self._stats.display()
        print(self._shade_call, "shade")
#####################################


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, days):
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self._harvest_season)
        print(" Nutritional value:", self._nutritional_value)

#####################################


def displayer(plant):
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    F = Flower("Rose", 15, 10, "red")
    T = Tree("Oak", 200, 365, 5)
    S = Seed("Sunflower", 80, 45, "yellow")
    A = Plant.anonymous()
    F.age_check(30)
    F.age_check(400)
    print("\n===", F.__class__.__name__)
    F.show()
    F._stats.display()
    F.grow(10)
    F.bloom(True)
    F.show()
    F._stats.display()
    print("\n===", T.__class__.__name__)
    T.show()
    T.produce_shade(0)
    T.display()
    T.grow(10)
    T.show()
    T.produce_shade(1)
    T.display()
    print("\n===", S.__class__.__name__)
    S.show()
    S.age(20)
    S.grow(30)
    S.bloom(True)
    S.show()
    S._stats.display()
    print("\n===", A.__class__.__name__)
    A.show()
    A._stats.display()
    print("\n=== Stat displayer")
    displayer(F)
    displayer(T)
    displayer(S)
    displayer(A)


if __name__ == "__main__":
    main()
