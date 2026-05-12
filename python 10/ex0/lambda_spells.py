#!/usr/bin/env python3

if __name__ == "__main__":
    main()

"""
Exercice
1 lire l exercice, lister les choses à apprendre
2 remplir le work instructions
3 Lire le w3school/autre concerne
4 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

Si bloqué:
-Voir exemples
-réexpliquer par GPT
-arrêter de se casser le crâne à voir plus compliqué
-faire morceau par morceau et implémenter
---------------------------------------------
Work instruction

[tutorials]
https://www.w3schools.com/python/python_lambda.asp

[authorized functions]
map, filter, sorted, min, max, round, sum, len

[Tools]
generator

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]
The Challenge
Create a file lambda_spells.py that contains functions demonstrating lambda
mastery:
Function Signatures:
def artifact_sorter(artifacts: list[dict]) -> list[dict]
def power_filter(mages: list[dict], min_power: int) -> list[dict]
def spell_transformer(spells: list[str]) -> list[str]
def mage_stats(mages: list[dict]) -> dict

Implementation Requirements
artifact_sorter(artifacts) - Sort magical artifacts:
• Use sorted() with a lambda to sort by ’power’ level (descending)
• Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}
• Return the sorted list

power_filter(mages, min_power) - Filter mages by power:
• Use filter() with a lambda to find mages with power >= min_power
• Each mage is a dict: {’name’: str, ’power’: int, ’element’: str}
• Return a list of filtered mages

spell_transformer(spells) - Transform spell names:
• Use map() with a lambda to add "* " prefix and " *" suffix
• Input: list of spell names (strings)
• Return a list of transformed spell names

mage_stats(mages) - Calculate statistics:
• Use lambdas with max(), min() to find:
• Most powerful mage’s power level
• Least powerful mage’s power level
• Average power level (rounded to 2 decimals)
• Return dict: {’max_power’: int, ’min_power’: int, ’avg_power’: float}

#################################################

G [general project instructions]
IV.1 Python Requirements
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• Exception handling should protect the data streams from corruption.
• Use type hints for all function signatures and return types.
• Focus on demonstrating functional programming patterns clearly.
• Each exercise should be in its own file with the specified name.
• Write clean, readable code that demonstrates your understanding.

IV.2 Authorized Imports
• typing module - For advanced type hints
• When using Callable as a type hint, use collections.abc
• itertools module - For advanced iteration patterns
• Essential modules for this project functools and operator will be specified
if allowed in each exercise.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized, but eval() and exec().
• Standard library modules as needed for the exercises 7 FuncMage Master the
Ancient Arts of Functional Programming

IV.3 Forbidden
• External libraries (no pip install)
• File I/O operations (focus on in-memory processing)
• Complex algorithms (keep focus on functional patterns)
• Using eval() or exec()
• Global variables (embrace functional purity when possible)

IV.4 Output Specifications Each exercise provides terminal examples showing
the suggested output format. While the core structure must be maintained,
you may customize messages to reflect your understanding of the file
operations, as long as the essential information is preserved.

During peer-review, you may be asked to explain functional programming
concepts, demonstrate how closures work, or show how decorators transform
functions. Focus on understanding the concepts, not just the implementation.
"""
