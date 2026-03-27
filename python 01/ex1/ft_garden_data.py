#!/usr/bin/env python3

def main() -> None:
    class Plant:
        def __init__(self, name: str, height: int, age: int):
            self.name = name
            self.height = height
            self.age = age

        def show(self):
            print(self.name, ": ", self.height, "cm, ", self.age, " days old",
                  sep="")

    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p1.show()
    p1 = Plant("Sunflower", 80, 45)
    p1.show()
    p1 = Plant("Cactus", 15, 120)
    p1.show()


if __name__ == "__main__":
    main()


"""
plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]
for p in plants:
    p.show()
"""
