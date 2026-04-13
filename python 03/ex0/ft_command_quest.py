#!/usr/bin/env python3
import sys


def main() -> None:
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
