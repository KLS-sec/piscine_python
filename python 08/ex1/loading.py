"""Exercice
1 lire l exercice, lister les choses à apprendre
2 remplir le work instructions
3 Lire le w3school/autre concerne
4 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

si bloqué
-Exemple
-GPT
-exo mal fait de tt facon, ne pas m'épuiser dessus
---------------------------------------------
G [tutorials]
https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=What%20is%20Pandas%3F,by%20Wes%20McKinney%20in%202008.
https://www.w3schools.com/python/numpy/numpy_intro.asp
python pandas
python numpy

[authorized functions / files to submit]




-ARRÊTE DE TE PRENDRE LA TETE, C EST SIMPLE





pandas, requests, matplotlib, numpy, sys, importlib
loading.py, requirements.txt, pyproject.toml

XXX[exercise instructions - ORGANIZED]
general
V    install numpy, pandas, matpotlib
    read their w3school tutorial

loading.py
    use pandas, numpy, matplotlib, poetry, pip
        numpy to generate data
        panda organise the data and add metadata (no need to learn more now)
        matplotlib to generate a graph with the data

        redo this part of the instructions

    create 2 regulating files
        pip
            use this codeline: pip freeze > requirements.txt
            to use to reinstall a setup: pip install -r requirements.txt
        poetry
            pyproject.toml

end:
    will nedd to show the use of pip and poetry (what is poetry?)

TODO
[exercise instructions - to reorganize]
Create a data analysis program called loading.py that:
• Uses pandas for data manipulation
• Uses numpy for numerical computations and to generate your simulated Matrix
data. It must be the source of your dataset — not hardcoded lists or range().
• Uses matplotlib for visualization
• Demonstrates the difference between pip and Poetry dependency management
• Includes proper dependency files for both approaches

Your program should analyze "Matrix data" (you can simulate this with sample
data) and generate a simple visualization.

By default, simulate your Matrix data using numpy. If you choose to fetch real
data from an external API, you are allowed to use requests — but it is not
required.

Requirements
• Create both requirements.txt (for pip) and pyproject.toml (for Poetry)
• Your program must handle missing dependencies gracefully
• Include a comparison function that shows installed package versions
• Show the differences between pip and Poetry through your program’s output

Your program should detect which packages are available and provide
helpful error messages if dependencies are missing.

Exceptionnally, flake8 and mypy errors are allowed for this exercise,
only for import errors. Nonetheless there is some mechanics and
implementation to avoid those errors, if you are curious and want dig
further.

G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check
this using mypy .
• Exception handling should protect the data streams from corruption.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized.
• Test your programs in different environments (with/without virtual
env, with/without dependencies).
"""
"""
# ex1/loading.py

from __future__ import annotations

import sys
import os
import importlib
from typing import Any


def safe_import(module_name: str) -> Any | None:
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def get_version(pkg: str) -> str:
    try:
        from importlib.metadata import version
        return version(pkg)
    except Exception:
        return "unknown"


def check_dependencies() -> dict[str, Any]:
    deps = {
        "numpy": safe_import("numpy"),
        "pandas": safe_import("pandas"),
        "matplotlib": safe_import("matplotlib"),
    }

    # optional dependency
    deps["requests"] = safe_import("requests")

    return deps


def print_dependency_status(deps: dict[str, Any]) -> bool:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    required = ["numpy", "pandas", "matplotlib"]
    ok = True

    for name in required:
        if deps[name] is None:
            print(f"[ERROR] {name} not installed")
            print(f"Install with: pip install {name} OR poetry add {name}")
            ok = False
        else:
            print(f"[OK] {name} ({get_version(name)}) - ready")

    if deps["requests"] is not None:
        print(f"[OK] requests ({get_version('requests')}) - optional API"
               " access ready")

    return ok


def generate_data(np: Any) -> Any:
    return np.random.normal(size=1000)


def process_data(pd: Any, data: Any) -> Any:
    df = pd.DataFrame(data, columns=["values"])
    df["normalized"] = (df["values"] - df["values"].mean()) / df["values"].std()
    return df


def visualize_data(plt: Any, df: Any) -> None:
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")


def show_environment_info() -> None:
    print("\nEnvironment info:")
    print(f"Python executable: {sys.executable}")
    print(f"Virtual env: {os.environ.get('VIRTUAL_ENV', 'None')}")


def show_package_manager_note() -> None:
    print("\nPackage management comparison:")
    print("- pip: installs from requirements.txt into environment")
    print("- poetry: manages env + dependencies via pyproject.toml")


def main() -> None:
    deps = check_dependencies()

    show_environment_info()
    show_package_manager_note()

    if not (deps["numpy"] and deps["pandas"] and deps["matplotlib"]):
        print("\nMissing dependencies. Aborting analysis.")
        return

    np = deps["numpy"]
    pd = deps["pandas"]
    plt = deps["matplotlib"].pyplot

    print("\nAnalyzing Matrix data...")
    data = generate_data(np)

    print("Processing 1000 data points...")
    df = process_data(pd, data)

    print("Generating visualization...")
    visualize_data(plt, df)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

"""
