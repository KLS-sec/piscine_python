#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: float, days: int):
            self.name = name
            self.height = height
            self.days = days

        def grow(self: float) -> float:
            return (self.cm + (0.8 * self.time))

        def age(self: int) -> int:
            return (self.days + self.time)

        def show(self, time: int):
            self.time = time
            print(self.name, ": ", self.grow(), "cm, ", self.age(),
                  " days old", sep="")





if __name__ == "__main__":
    main()
