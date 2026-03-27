#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: float, days: int):
            self.name = name
            self.height = height
            self.days = days

        def grow(self: float) -> float:
            return (self.height + (0.8 * self.time))

        def age(self: int) -> int:
            return (self.days + self.time)

        def show(self, time: int):
            self.time = time
            print(self.name, ": ", self.grow(), "height, ", self.age(),
                  " age old", sep="")

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    Plant("Rose", 25, 30).show(0)
    print("Created: ", end="")
    Plant("Oak", 200, 365).show(0)
    print("Created: ", end="")
    Plant("Cactus", 5, 90).show(0)
    print("Created: ", end="")
    Plant("Sunflower", 80, 45).show(0)
    print("Created: ", end="")
    Plant("Fern", 15, 120).show(0)


if __name__ == "__main__":
    main()
