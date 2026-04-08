#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    value: list[str] = ["25", "abc", "100", "-50"]
    for n in value:
        print("\nInput data is '", n, "'", sep="")
        try:
            x: int = input_temperature(n)
            print("Temperature is now ", x, "°C", sep="")
        except Exception as err:
            print("Caught input_temperature error:", err)


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
