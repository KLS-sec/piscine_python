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

    if (new_file_name := input("Enter new file name (or empty): ")) == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")
    # error handling, just to train
    try:
        file: IO[str] = open(new_file_name, "w")
        file.write(transformed)
        file.close()
    except Exception as err:
        print(f"Error opening file '{new_file_name}': {err}")
        return
    print(f"Data saved in file '{new_file_name}'")


if __name__ == "__main__":
    main()

"""
gpt emmerde avec des petits details hors contexte

import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.write(), io.close(), print(), input()


1 retake previous code

improve it
2 add # at the end of each line
3 display the new content
4 input the name of a file
a if no name does not save anything
b create a new file and save in it if a name is given (replace if it already
  exist)


Use the code created for the previous exercise. At the end of the script,
improve the code to:
• Add a special archive character (the # character) at the end of each
line
• Display the new content
• Ask the user for the name of the file to save to, or leave it empty to avoid
saving anything
• Save the new content if a file name is provided and display a new ending
message
Create the file or replace it if it already exists.
"""
