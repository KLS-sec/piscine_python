#!/usr/bin/env python3
import sys


def main():
    args = sys.argv
    i = 1
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if len(args) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for x in args[1:]:
            print(f"Argument {i}: {x}")
            i += 1
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
"""
import sys, sys.argv, len(), print()

how programs can receive messages from their users
introduce lists.
Before building your own lists, let’s manipulate a list that already exists:
the command-line parameters, available through the module sys.
The structure is similar to the one in C: an array of strings. Explore how to
access and manipulate list elements.
Build a simple script that shows the data received as command-line parameters.
Mimic the example below.


if __name__ == "__main__":
    main()

args = sys.argv[:1] to ignore program name

def main():
    args = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if len(args) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for i, x in enumerate(args[1:], start=1):
            print(f"Argument {x}: {i}")
    print(f"Total arguments: {len(args)}")

    """
