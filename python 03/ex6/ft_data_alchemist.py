#!/usr/bin/env python3

import random


def capital_entry(names: list) -> list[str]:
    good_entry = []
    for x in names:
        if x == x.capitalize():
            good_entry.append(x)
    return (good_entry)


def capitalize_entry(names: list) -> list[str]:
    capitalized = []
    for x in names:
        x.capitalize()
        capitalized.append(x)


def main() -> None:
    # A
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
             'kevin', 'Liam']

if __name__ == "__main__":
    main()

"""
import random, random.*, print(), len(), sum(), round()
list + dictionnary

DONE
A - create a LIST of player name, some capitalised, other not

TODO
create 2 comprehensions:
1 create a new list that take all names and capitalize them
2 create list with names that were ALREADY capitalized

with a third comprehension:
create a dictionnary with the capitalized list (comprehension 1)
names are the keys
values are randomly generated scores (in a range)

calculate the average score

with a fourth comprehension
create another dictionnary with only the name of thoses above average

###########################################################



This exercise requires the use of list and dictionary comprehensions
to transform and filter data efficiently. These are fundamental Python
features for data processing.

Create a list of player names, where some are capitalized and others
are not. Build two list comprehensions: the first one creates a new
list with all names capitalized, the second one creates a new list
with only the capitalized names from the initial list.

Now, let’s create a dictionary from this full capitalized list of
player names. Names will be the keys, and values will be randomly
generated scores in a defined range.
Of course, a comprehension will build this dictionary.
Then a second dict will be created, with scores higher than
the average, also using a comprehension.

"""
