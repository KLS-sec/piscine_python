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


"""
AI checked
mypy
flake8


import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.close(), print()

V 1 utiliser argv pour print le nom du fichier
V 2 gerer pb d argv
V 3 header + accessing file
V 4 gerer les differents types d erreurs
V 5 afficher le nom du fichier (voir phrase exemple)
V 6 afficher contenus
V 7 footer (conditionnel)

X fermeture (dois arriver dans tt les cas si ouverture a eu lieu)

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
"""

if __name__ == "__main__":
    main()


"""
"""
