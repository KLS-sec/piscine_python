#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    arg_values: list[int] = []

    for x in args:
        try:
            arg_values.append(int(x))
        except ValueError:
            print(f"Invalid parameter: '{x}'")

    if len(arg_values) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
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
    print(f"Average score: {round(average_score, 1)}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
