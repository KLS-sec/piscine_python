# !/usr/bin/env python3


def main() -> None:
    pass


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

G [tutorials]
Pydantic
pip install pydantic
https://www.geeksforgeeks.org/python/introduction-to-python-pydantic-library/


[authorized functions]

[Tools]
• data_generator.py - Generate realistic test data for all exercises
• data_exporter.py - Export data in JSON, CSV, and Python formats
• generated_data/ - Pre-generated datasets ready to use

[needed files]

[exercise instructions - organized + general goal + explanation by gpt]

[exercise instructions - original]

G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check this using mypy.
• Exception handling should protect the data streams from corruption.
• All standard classes and collections are authorized, along with their methods
(int, str, list, dict, etc.).
• All built-in functions are authorized. • Use pip as package manager
• You must use Virtual environments (recommended: venv, virtualenv, or conda)
• You must use which Pydantic 2.x for every exercise. (It must be installed
via pip). Only other modules will be listed in each exercise’s Allowed section

- Authorized imports: You may import JSON and CSV data from the tools
directory. Standard library modules (json, csv, datetime, etc.) are allowed.

- Important: This activity focuses on Pydantic v2 syntax. Avoid deprecated
decorators like @validator - use @model_validator for custom validation
instead.


-BaseModel
The foundation of all Pydantic models. Inherit from BaseModel to create
validated data classes.
-Field
Use Field(...) to add validation constraints, descriptions, and default values
to model attributes.
-model_validator
Use the @model_validator(mode=’after’) decorator for custom validation logic
that runs after Pydantic’s built-in validation. This replaces the deprecated
@validator decorator from Pydantic v1.
"""
