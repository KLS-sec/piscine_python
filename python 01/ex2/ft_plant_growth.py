#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: int, days: int):
            self.name = name
            self.height = height
            self.days = days

        def grow(self: float) -> float:
            return (self.height + (0.8 * self.time))

        def age(self: int) -> int:
            return (self.days + self.time)

        def show(self, time: int):
            self.time = time
            print(self.name, ": ", self.grow(), "cm, ", self.age(),
                  " days old", sep="")

    x = range(0, 7)
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25, 30)
    for n in x:
        print("=== Day ", n + 1, " ===", sep="")
        p1.show(n)
    print("Growth this week: ", round(n * 0.8, 2), "cm", sep="")


if __name__ == "__main__":
    main()


"""
• Reuse your Plant class from Exercise 1
FAIT

• Plants need to be able to grow() and age() on their own (i.e., these
will be methods of the class)

• Simulate a week of growth for a plant, then access the data in the
class to get the final height and display the total week increase.

• Consider how the plant should change over time when using grow() and age().
Different plants can evolve differently.
"""
