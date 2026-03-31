#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    if int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    if int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    value: list[str] = ["25", "abc", "100", "-50"]
    for n in value:
        print("Input data is '", n, "'", sep="")
        try:
            x: int = input_temperature(n)
            print("Temperature is now ", x, "°C\n", sep="")
        except Exception as err:
            print("Caught input_temperature error:", err, "\n")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
