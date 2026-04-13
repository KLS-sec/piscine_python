#!/usr/bin/env python3

import sys
from typing import IO


if __name__ == "__main__":
    main()


import sys
from typing import IO


def read_file(filename: str) -> None:
    file: IO

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "rt")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---\n")
    try:
        content = file.read()
        print(content, end="")  # avoid double newline
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        file.close()
        return

    print("\n---")
    file.close()
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
"""