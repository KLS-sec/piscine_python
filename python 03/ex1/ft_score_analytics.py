#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    arg_values: list[int] = []

    for x in args:
        try:
            arg_values.append(int(x))
        except Exception:
            print(f"Invalid parameter: '{x}'")

    if len(arg_values) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
        return

    total_players: int = len(arg_values)
    total_score: int = sum(arg_values)
    average_score: float = total_score / total_players
    high_score: int = max(arg_values)
    low_score: int = min(arg_values)
    score_range: int = high_score - low_score

    print(f"Scores processed: {arg_values}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()

"""
import sys, sys.argv, len(), sum(), max(), min(), print()

This exercise requires you to use lists to store scores and try/except blocks
to handle invalid input gracefully (e.g., when a user provides non-numeric
values).

You will get game scores as command-line parameters. You need to:
• Process the command-line arguments
• Handle the various erroneous cases (no arguments, non-numeric values) with
appropriate messages
• Create a new list to store and organize the scores
• Calculate some basic stats that would make any game player happy (number,
total, average, max, min, and range)
• Make the output look cool enough to impress your gaming buddies (you can
mimic the example again)
• If both valid and invalid inputs are provided via the command line, discard
the invalid ones and proceed with the remaining valid inputs unless none
remain.
"""
