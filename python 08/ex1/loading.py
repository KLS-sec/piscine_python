import importlib
from importlib.metadata import version


def main() -> None:
    try:
        np = importlib.import_module("numpy")
        pd = importlib.import_module("pandas")
        mpl = importlib.import_module("matplotlib.pyplot")
    except Exception as err:
        print(f"Error, missing dependencie: {err}")
        print("pip:\nUse <pip install -r requirements.txt> in the venv to"
              " instal dependencies # pip")
        return

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    p = version("pandas")
    q = version("numpy")
    r = version("matplotlib")
    print(f"[OK] {p} - Data manipulation ready")
    print(f"[OK] {q} - Numerical computation ready")
    print(f"[OK] {r} - Visualization ready")

    print("\nAnalyzing Matrix data...")
    array = np.random.normal(size=1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(array, columns=["values"])
    print("Generating visualization...")
    mpl.hist(df["values"], bins=30)
    mpl.title("Matrix Data Distribution")
    mpl.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


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

si bloqué
-Exemple
-GPT
-exo mal fait de tt facon, ne pas m'épuiser dessus
---------------------------------------------
G [tutorials]
https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=What%20is%20Pandas%3F,by%20Wes%20McKinney%20in%202008.
https://www.w3schools.com/python/numpy/numpy_intro.asp
https://www.w3schools.com/python/matplotlib_intro.asp
https://python-poetry.org/docs/basic-usage/
https://pypi.org/project/poetry/


[authorized functions / files to submit]
pandas, requests, matplotlib, numpy, sys, importlib
loading.py, requirements.txt, pyproject.toml

XXX[exercise instructions - ORGANIZED]
general
V    install numpy, pandas, matpotlib
    read their w3school tutorial

loading.py
    use pandas, numpy, matplotlib, poetry, pip
        numpy
            generate 1000 data points
        panda organise the data and add metadata (no need to learn more now)
            ???
        matplotlib to generate a graph with the data
            creer une bete courbe

        redo this part of the instructions

create 2 regulating files
    pip
        ****use this codeline:
            pip freeze > requirements.txt
        ****to use to reinstall a setup in the existing venv
            pip install -r requirements.txt
    poetry
        pyproject.toml

autre:
    voir importlib
    voir exemples pour details en plus

end:
    will nedd to show the use of pip and poetry (what is poetry?)

    poetry
        create m.toml
        creer .toml
            python3 -m poetry init --no-interaction
        fill .toml
            python3 -m poetry add "numpy<2.0" matplotlib "pandas<3.0"
        intall the env
            python3 -m poetry install --no-root
        use the loading.py without opening the venv
            python3 -m poetry run python loading.py
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

################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
"""
