#!/usr/bin/env python3

def garden_operations(operation_number) -> None:
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
print(), open(), int()

type() is forbiden

###########################

main only if needed
if __name__ == "__main__":
    main()

• All functions and methods must include type hints: use mypy to
  check your code
• Each exercise must be in its own file
• Focus on demonstrating basic error handling concepts clearly
• Show both normal operations and error scenarios
• Use built-in exceptions appropriately
• Keep solutions simple and focused on learning
• Your programs must never crash

Exception Handling: All exercises in this module require the use of
try/except blocks for error handling. Python keywords such as
’try’, ’except’, ’finally’, and ’raise’ are fundamental language
features and do not need to be listed in authorized functions.

You may use any built-in exception types necessary to complete
the exercises, including but not limited to, ValueError, TypeError,
ZeroDivisionError, FileNotFoundError, KeyError, IndexError,
AttributeError, and the base Exception class. Each exercise
description may include which exception types are most appropriate
for that specific task.

mypy will display an error for the faulty code that raises the
TypeError. That’s its job! So, to test this exception, we need
to keep this error on purpose.

#####################################

#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    ""
    Triggers different exceptions depending on operation_number.
    ""
    if operation_number == 0:
        int("abc")  # ValueError
    elif operation_number == 1:
        1 / 0  # ZeroDivisionError
    elif operation_number == 2:
        open("/non/existent/file")  # FileNotFoundError
    elif operation_number == 3:
        "hello" + 5  # TypeError
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("Testing multiple exception catch...")
    try:
        garden_operations(0)
    except (ValueError, TypeError) as e:
        print(f"Caught multiple types: {e}")

    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
"""
