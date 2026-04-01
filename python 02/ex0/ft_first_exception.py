#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    value: list[str] = ["25", "abc"]
    for n in value:
        print("Input data is '", n, "'", sep="")
        try:
            x: int = input_temperature(n)
            print("Temperature is now ", x, "°C\n", sep="")
        except Exception as err:
            print("Caught input_temperature error:", err, "\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

"""
checked with gpt
"""
