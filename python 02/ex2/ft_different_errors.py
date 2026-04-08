#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")                  # ValueError
    elif operation_number == 1:
        1 / 0                       # ZeroDivisionError
    elif operation_number == 2:
        open("/non/existent/file")  # FileNotFoundError
    elif operation_number == 3:
        "hello" + 5                 # TypeError
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for n in range(5):
        print(f"Testing operation {n}...")
        try:
            garden_operations(n)
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")

    try:
        garden_operations(0)
    except (ValueError, TypeError) as err:
        print(f"\nMltiples errors test: {err}")

    print("\nAll error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()

"""
mypy will display an error for the faulty code that raises the
TypeError. That’s its job! So, to test this exception, we need
to keep this error on purpose.
"""
