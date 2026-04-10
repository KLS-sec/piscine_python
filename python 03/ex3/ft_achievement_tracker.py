#!/usr/bin/env python3

import random

achievement = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
               'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
               'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
               'Boss Slayer', 'Bronze', 'Silver', 'Gold', 'Platinum']


def gen_player_achievement() -> set:
    player_set = set()
    i = 0
    while i < 5:
        player_set.add(random.choice(achievement))
        i += 1
    return player_set


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    all_achievements = set(achievement)
    alice_set = gen_player_achievement()
    bob_set = gen_player_achievement()
    charlie_set = gen_player_achievement()
    dylan_set = gen_player_achievement()

    print(f"Player Alice: {alice_set}")
    print(f"Player Bob: {bob_set}")
    print(f"Player Charlie: {charlie_set}")
    print(f"Player Dylan: {dylan_set}")
    print(f"\nAll distinct achievements: {all_achievements}")
    print("\nCommon achievements:",
          f"{alice_set.intersection(bob_set, charlie_set, dylan_set)}")

    print(f"\nOnly Alice has: {alice_set.difference(bob_set, charlie_set,
                                                    dylan_set)}")
    print(f"Only Bob has: {bob_set.difference(alice_set, charlie_set,
                                              dylan_set)}")
    print(f"Only Charlie has: {charlie_set.difference(alice_set, bob_set,
                                                      dylan_set)}")
    print(f"Only Dylan has: {dylan_set.difference(alice_set, bob_set,
                                                  charlie_set)}")

    print(f"\nAlice is missing: {all_achievements.difference(alice_set)}")
    print(f"Bob is missing: {all_achievements.difference(bob_set)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie_set)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan_set)}")


if __name__ == "__main__":
    main()
