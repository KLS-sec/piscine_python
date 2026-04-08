#!/usr/bin/env python3

class Plant:
    class _Stats:  # nested class (internal use)
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
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

    def display_stats(self) -> None:
        self._stats.display()

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age
        self._stats = Plant._Stats()

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return (self._age)

    def get_height(self) -> float:
        return (float(self._height))

    def set_age(self, age: int) -> None:
        if age < 0:
            print(self._name, ":Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print("Age updated: ", self._age, " days", sep="")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self._name, ":Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print("Height updated: ", self._height, "cm", sep="")

    def grow(self, days: int) -> None:
        self._height += (days * 0.8)
        self._stats.called_grow()

    def age(self, days: int) -> None:
        self._age += days
        self._stats.called_age()

    def show(self) -> None:
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._age, " days old",
              sep="")
        self._stats.called_show()

    @staticmethod
    def age_check(value: int) -> None:
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

    def bloom(self, blooming: bool) -> None:
        self._blooming = blooming

    def show(self) -> None:
        super().show()
        print(" Color:", self._color)
        if self._blooming:
            print("", self._name, "is blooming beautifully!")
        else:
            print("", self._name, "has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_number = 0

    def bloom(self, blooming: bool) -> None:
        super().bloom(blooming)
        if blooming:
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

    def produce_shade(self, shader: bool) -> None:
        if shader:
            print("Tree ", self._name, " now produces a shade of ",
                  self._height, "cm long and ", self._trunk_diameter,
                  "cm wide.", sep="")
        self._shade_call += 1

    def show(self) -> None:
        super().show()
        print(" Trunk diameter: ", self._trunk_diameter, "cm long", sep="")

    def display(self) -> None:
        self.display_stats()
        print("", self._shade_call, "shade")
#####################################


def displayer(target: Plant) -> None:
    target.display_stats()


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
    print(f"[statistics for {F.get_name()}]")
    F.display_stats()
    print(f"[asking the {F.get_name()} to grow and bloom]")
    F.grow(10)
    F.bloom(True)
    F.show()
    print(f"[statistics for {F.get_name()}]")
    F.display_stats()
    print("\n===", T.__class__.__name__)
    T.show()
    print(f"[statistics for {T.get_name()}]")
    T.display()
    print(f"[asking the {T.get_name()} to produce shade]")
    T.produce_shade(True)
    print(f"[statistics for {T.get_name()}]")
    T.display()
    print("\n===", S.__class__.__name__)
    S.show()
    print(f"[make {S.get_name()} grow, age and bloom]")
    S.age(20)
    S.grow(30)
    S.bloom(True)
    S.show()
    print(f"[statistics for {S.get_name()}]")
    S.display_stats()
    print("\n=== Anonymous")
    A.show()
    A.display_stats()
    print("\n=== Stat displayer")
    displayer(F)
    displayer(T)
    displayer(S)
    displayer(A)


if __name__ == "__main__":
    main()
