# !/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


"""
Create a Pydantic model with these validated fields:
    • station_id: String, 3-10 characters
    • name: String, 1-50 characters
    • crew_size: Integer, 1-20 people
    • power_level: Float, 0.0-100.0 percent
    • oxygen_level: Float, 0.0-100.0 percent
    • last_maintenance: DateTime field
    • is_operational: Boolean, defaults to True
    • notes: Optional string, max 200 characters
"""


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    StationOne = SpaceStation(
                  station_id="ISS001",
                  name="International Space Station",
                  crew_size=6,
                  power_level=85.5,
                  oxygen_level=92.3,
                  last_maintenance=datetime.fromisoformat("2026-05-01T12:"
                                                          "00:00+00:00"),
                  is_operational=True)

    if StationOne.is_operational:
        x = "Operational"
    else:
        x = "Shut-Down"

    print("Valid station created:")
    print(f"ID: {StationOne.station_id}")
    print(f"Name: {StationOne.name}")
    print(f"Crew: {StationOne.crew_size} people")
    print(f"Power: {StationOne.power_level}%")
    print(f"Oxygen: {StationOne.oxygen_level}%")
    print(f"Status: {x}")

    print("\n========================================")

    try:
        StationTwo = SpaceStation(
                    station_id="12345678",
                    name="ISS",
                    crew_size=66,
                    power_level=85.5,
                    oxygen_level=92.3,
                    last_maintenance=datetime.fromisoformat("2026-05-01T12:"
                                                            "00:00+00:00"),
                    is_operational=True)
    except ValidationError as err:
        e = err.errors()[0]["msg"]
        print(f"Expected validation error:\n{e}")
        return

    print(f"Station Two ID: {StationTwo.station_id}")


if __name__ == "__main__":
    main()

"""
Exercice
X regarder liste pauses

Si bloqué:
-Voir exemples
-réexpliquer par GPT
-arrêter de se casser le crâne à voir plus compliqué
-faire morceau par morceau et implémenter
-------------------------------------------------

Work instruction

G [tutorials]
Pydantic
pip install pydantic
https://www.geeksforgeeks.org/python/introduction-to-python-pydantic-library/
https://pydantic.dev/docs/validation/latest/get-started/
https://pydantic.dev/docs/validation/latest/concepts/fields/#_top
https://pydantic.dev/docs/validation/latest/api/pydantic/standard_library_typess

[authorized functions]
None

[Tools]
• data_generator.py - Generate realistic test data for all exercises
• data_exporter.py - Export data in JSON, CSV, and Python formats
• generated_data/ - Pre-generated datasets ready to use

[needed files]
space_station.py
-------------------------------------------------

[exercise instructions - organized + general goal + explanation by gpt]
Goal:
Learn to use Pydantic
(model creation, BaseModel, Field validation)

Create a validation system for data

demonstraiting main()
    -create 1 valid space station
        -print the info
    -create 1 invalid station
        -print the error message

-------------------------------------------------

[exercise instructions - original]
Demonstration Function
Include a main() function that:
• Creates a valid space station instance
• Displays the station information clearly
• Attempts to create an invalid station (e.g., crew_size > 20)
• Shows the validation error message
-------------------------------------------------

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

Notes:
install pydantic and additionnal settings
    pip install pydantic pydantic-settings

#################################################

stock:
Objective: Learn basic Pydantic model creation with BaseModel and
Field validation.

IV.1 Background
The Cosmic Data Observatory monitors hundreds of space stations across the
galaxy.
Each station reports vital statistics including crew size, power levels,
and operational status. Your first task is to create a validation system
for this critical data.

IV.2 Requirements
SpaceStation Model
Create a Pydantic model with these validated fields:
• station_id: String, 3-10 characters
• name: String, 1-50 characters
• crew_size: Integer, 1-20 people
• power_level: Float, 0.0-100.0 percent
• oxygen_level: Float, 0.0-100.0 percent
• last_maintenance: DateTime field
• is_operational: Boolean, defaults to True
• notes: Optional string, max 200 characters

Demonstration Function
Include a main() function that:
• Creates a valid space station instance
• Displays the station information clearly
• Attempts to create an invalid station (e.g., crew_size > 20)
• Shows the validation error message
"""
