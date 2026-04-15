#!/usr/bin/env python3

import sys
from typing import IO


def extractor(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename, "rt")
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")
        return

    print("---\n")
    print(f"{file.read()}", end="")
    print("\n---")
    file.close()
    print(f"File '{filename}' closed.")


def liner(filename: str) -> str:
    source: IO[str] = open(filename, "rt")
    returner: str = ""
    for x in source:
        returner += x.rstrip("\n") + "#\n"
    source.close()
    return returner


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    extractor(sys.argv[1])

    transformed: str = liner(sys.argv[1])
    print("\nTransform data:")
    print("---\n")
    print(transformed)
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()  # buffer problem when print does not end with "\n"
    new_file_name: str = sys.stdin.readline().rstrip("\n")

    if new_file_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")
    # error handling, just to train
    try:
        file: IO[str] = open(new_file_name, "w")
        file.write(transformed)
        file.close()
    except Exception as err:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file_name}': "
                         f"{err}\n")
        print("Data not saved.")
        return
    print(f"Data saved in file '{new_file_name}'")


if __name__ == "__main__":
    main()
