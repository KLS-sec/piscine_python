#!/usr/bin/env python3

def main() -> None:
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print("Plant: ", name)
    print("Height: ", height, "cm")
    print("Age: ", age, " days")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()

"""
name = "Rose"
height = 25
age = 30

if __name__ == "__main__":
    print("=== Welcome to My {} ===".format("Garden"))
    print("Plant: ", name)
    print(f"Height: {height}cm")
    print("Age: {} days".format(age))
    print("=== End of Program ===")
"""
