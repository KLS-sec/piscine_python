# !/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    @classmethod
    def cast_ints(cls, value: Any) -> Any:
        if isinstance(value, int):
            return str(value)
        else:
            return value


def main() -> None:
    pass


if __name__ == "__main__":
    main()


"""
Exercice
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
https://pydantic.dev/docs/validation/latest/concepts/validators/#model-validators
https://pydantic.dev/docs/validation/latest/concepts/validators/#field-after-validator
https://www.geeksforgeeks.org/python/enum-in-python/

[authorized functions]
None

[Tools]
• data_generator.py - Generate realistic test data for all exercises
• data_exporter.py - Export data in JSON, CSV, and Python formats
• generated_data/ - Pre-generated datasets ready to use

[needed files]

[exercise instructions - organized + general goal + explanation by gpt]
goal:
use @model_validator


Enum: (voir exemples)
    -Define contact type
        -radio
        -visual
        -physical
        -telepathic

AlienContact: Pydantic model (BaseModel)
    • contact_id: String, 5-15 characters
    • timestamp: DateTime of contact
    • location: String, 3-100 characters
    • contact_type: ContactType enum
    • signal_strength: Float, 0.0-10.0 scale
    • duration_minutes: Integer, 1-1440 (max 24 hours)
    • witness_count: Integer, 1-100 people
    • message_received: Optional string, max 500 characters
    • is_verified: Boolean, defaults to False

Cunstom Validation rules
    -@model_validator(mode=’after’)
        • Contact ID must start with "AC" (Alien Contact)
        • Physical contact reports must be verified
        • Telepathic contact requires at least 3 witnesses
        • Strong signals (> 7.0) should include received messages


----------------------------------------------------------------------------
[exercise instructions - original]
----------------------------------------------------------------------------
G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check this using mypy.
• Exception handling should protect the data streams from corruption.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
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
