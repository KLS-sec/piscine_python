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


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    station_one = SpaceStation(
                  station_id="ISS001",
                  name="International Space Station",
                  crew_size=6,
                  power_level=85.5,
                  oxygen_level=92.3,
                  last_maintenance=datetime.fromisoformat("2026-05-01T12:"
                                                          "00:00+00:00"),
                  is_operational=True)

    if station_one.is_operational:
        x = "Operational"
    else:
        x = "Shut-Down"

    print("Valid station created:")
    print(f"ID: {station_one.station_id}")
    print(f"Name: {station_one.name}")
    print(f"Crew: {station_one.crew_size} people")
    print(f"Power: {station_one.power_level}%")
    print(f"Oxygen: {station_one.oxygen_level}%")
    print(f"Status: {x}")

    print("\n========================================")

    try:
        station_two = SpaceStation(
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

    print(f"Station Two ID: {station_two.station_id}")


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

Notes:
install pydantic and additionnal settings
    pip install pydantic pydantic-settings
"""
