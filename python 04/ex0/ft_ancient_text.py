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


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    extractor(sys.argv[1])


if __name__ == "__main__":
    main()
