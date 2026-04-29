import sys
import os

if sys.prefix != sys.base_prefix:
    print("\nMATRIX STATUS: Welcome to the construct")
    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)
    print("\nSUCCESS: You're in an isolated environment!\nSafe to install"
          " packages without affecting\nthe global system.")
    print("\nPackage installation path:")
    print(sys.path)

else:
    print("\nMATRIX STATUS:  You're still plugged in")
    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!\n"
          "The machines can see everything you install.")
    print("\nTo enter the construct, run:\n"
          "python3 -m virtualenv myfirstproject\n"
          "source myfirstproject/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")

"""
4 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants (utiliser checklist projet)
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

si bloqué
-Exemple
-GPT
-exo mal fait de tt facon, ne pas m'épuiser dessus

---------------------------------------------

G [tutorials]
python virtual environment / global environment
https://www.w3schools.com/python/python_virtualenv.asp
https://www.geeksforgeeks.org/python/python-virtual-environment/
https://docs.python.org/3/library/venv.html
https://packaging.python.org/en/latest/specifications/virtual-environments/
https://stackoverflow.com/questions/1871549/how-to-determine-if-python-is-running-inside-a-virtualenv



[IMPORTANT]
python3 -m pip install virtualenv
    installation des packages permetant de faire du venv
python3 -m virtualenv myfirstproject
    creation de l environnement
source myfirstproject/bin/activate
    activer
deactivate
    desactiver
tout pareil a partir de la, juste virtualenv au lieu de venv

[authorized functions]
sys, os, site modules, print()

TODO[exercise instructions - to reorganize]

construct.py
    detect if it is running inside a virtual env
        -sys.prefix != sys.base_prefix
        -if NOT in venv
            -give explanation about how to open it
    show informations about the python environment, SEE EXEMPLES
        -adress of curently used python
        -if in venv: venv path
        -if in venv: package instalation path
    Must work in and out venv


Create a program called construct.py that:
• Detects whether it is running inside a virtual environment
• Displays information about the current Python environment
• Provides instructions for creating and activating a virtual
  environment if none is detected
• Shows the difference between global and virtual environment
  package locations

Your program should work both inside and outside virtual
environments, providing different outputs for each scenario.

Do not submit your virtual environnement in your repository. You
must be able to create a new one during review if needed.

----------------------------------------

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
