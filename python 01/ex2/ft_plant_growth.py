#!/usr/bin/env python3
# if __name__ == "__main__":

# print(), range(), round()

def main() -> None:
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def show(self):
            print(f"{self.name}: {self.height}cm, {self.age} days old")

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
• Reuse your Plant class from Exercise 1
FAIT

• Plants need to be able to grow() and age() on their own (i.e., these
will be methods of the class)

• Simulate a week of growth for a plant, then access the data in the
class to get the final height and display the total week increase.

• Consider how the plant should change over time when using grow() and age().
Different plants can evolve differently.
"""
