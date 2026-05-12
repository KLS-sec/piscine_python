# !/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class CrewRanks(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    rank: CrewRanks
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    budget_millions: float = Field(ge=1.0, le=10000.0)
    mission_status: str = "planned"
    crew: list[CrewMember] = Field(min_length=1, max_length=12)

    @model_validator(mode='after')
    def checker(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Missiom ID must start with 'M'")

        for x in self.crew:
            if not x.is_active:
                raise ValueError("Mission list an innactive crew member")

        y = 0
        for x in self.crew:
            if x.rank in (CrewRanks.commander, CrewRanks.captain):
                y += 1
        if y == 0:
            raise ValueError("Mission must have at least one Commander or"
                             " Captain")

        if self.duration_days > 365:
            z = 0
            for x in self.crew:
                if x.years_experience >= 5:
                    z += 1
            if z < len(self.crew) / 2:
                raise ValueError("Mission must have more experienced members")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    shepard = CrewMember(
            member_id="123",
            name="Shepard",
            age=30,
            specialization="Specter",
            rank=CrewRanks.commander,
            years_experience=10,
            is_active=True)

    joker = CrewMember(
            member_id="124",
            name="Joker",
            age=30,
            specialization="Pilot",
            rank=CrewRanks.lieutenant,
            years_experience=10,
            is_active=True)

    edi = CrewMember(
            member_id="125",
            name="EDI",
            age=30,
            specialization="Onboard AI",
            rank=CrewRanks.cadet,
            years_experience=1,
            is_active=True)

    cerberus_agents: list[CrewMember] = [shepard, joker, edi]

    normandy = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2026-05-01T12:00:00+00:00"),
        duration_days=900,
        budget_millions=2500.0,
        mission_status="Ongoing",
        crew=cerberus_agents
    )
    print(f"Mission: {normandy.mission_name}")
    print(f"ID: {normandy.mission_id}")
    print(f"Destination: {normandy.destination}")
    print(f"Duration: {normandy.duration_days}")
    print(f"Budget: {normandy.budget_millions}")
    print(f"Crew size: {len(normandy.crew)}")
    print("Crew members:")
    for agent in normandy.crew:
        print(f"- {agent.name} ({agent.rank.value}) - {agent.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    sherpardd = CrewMember(
            member_id="123",
            name="Shepard",
            age=30,
            specialization="Specter",
            rank=CrewRanks.commander,
            years_experience=10,
            is_active=True)

    jokerr = CrewMember(
            member_id="124",
            name="Joker",
            age=30,
            specialization="Pilot",
            rank=CrewRanks.lieutenant,
            years_experience=1,
            is_active=True)

    edii = CrewMember(
            member_id="125",
            name="EDI",
            age=30,
            specialization="Onboard AI",
            rank=CrewRanks.cadet,
            years_experience=1,
            is_active=True)

    cerberus_agentss: list[CrewMember] = [sherpardd, jokerr, edii]

    try:
        normandyy = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2026-05-01T12:00:00+00:00"),
            duration_days=900,
            budget_millions=2500.0,
            mission_status="Ongoing",
            crew=cerberus_agentss
        )
    except ValidationError as err:
        e = err.errors()[0]["msg"]
        print(e)
        return
    normandyy = normandyy


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


[authorized functions]
None

[Tools]
• data_generator.py - Generate realistic test data for all exercises
• data_exporter.py - Export data in JSON, CSV, and Python formats
• generated_data/ - Pre-generated datasets ready to use

[needed files]
space_crew.py
---------------------------------------------------------
[exercise instructions - organized + general goal + explanation by gpt]

objective: nested pydantic models + complex data relationship

XXX
Enum rewRank
    -cadet
    -officer
    -lieutenant
    -captain
    -commander

CrewMember Model
    • member_id: String, 3-10 characters
    • name: String, 2-50 characters
    • rank: Rank enum
    • age: Integer, 18-80 years
    • specialization: String, 3-30 characters
    • years_experience: Integer, 0-50 years
    • is_active: Boolean, defaults to True

SpaceMission Model
    • mission_id: String, 5-15 characters
    • mission_name: String, 3-100 characters
    • destination: String, 3-50 characters
    • launch_date: DateTime
    • duration_days: Integer, 1-3650 days (max 10 years)
    • crew: List of CrewMember, 1-12 members
    • mission_status: String, defaults to "planned"
    • budget_millions: Float, 1.0-10000.0 million dollars

In SpaceMission
    -@model_validator(mode=’after’)
        • Mission ID must start with "M"
        • Must have at least one Commander or Captain
        • Long missions (> 365 days) need 50% experienced crew (5+ years)
        • All crew members must be active

TODO
main test

[exercise instructions - original]

Think About: How does Pydantic handle validation of nested models? What happens
when a CrewMember fails validation within a SpaceMission?

---------------------------------------------------------
G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check this using mypy .
• Exception handling should protect the data streams from corruption.
• All standard classes and collections are authorized, along with their
  methods (int, str, list, dict, etc.).
• All built-in functions are authorized.
• Use pip as package manager
• You must use Virtual environments (recommended: venv, virtualenv, or conda)
• You must use which Pydantic 2.x for every exercise. (It must be installed
  via pip). Only other modules will be listed in each exercise’s Allowed
  section

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
