# !/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def checker(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if not self.is_verified and self.contact_type == ContactType.physical:
            raise ValueError("Physical contact must be verified")
        if (self.witness_count < 3 and
           self.contact_type == ContactType.telepathic):
            raise ValueError("Telepathic contact "
                             "requires at least 3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals must include a message")

        return self


def main() -> None:
    normandy = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-05-01T12:"
                                             "00:00+00:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True)

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {normandy.contact_id}")
    print(f"Type: {normandy.contact_type.value}")
    print(f"Location: {normandy.location}")
    print(f"Signal: {normandy.signal_strength}/10")
    print(f"Duration: {normandy.duration_minutes} minutes")
    print(f"Witnesses: {normandy.witness_count}")
    print(f"Message: '{normandy.message_received}'")

    print("\n======================================")
    print("Expected validation error:")
    try:
        boom = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime.fromisoformat("2026-05-01T12:"
                                                 "00:00+00:00"),
                location="Area 51, Nevada",
                contact_type=ContactType.telepathic,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=2,
                message_received="'Greetings from Zeta Reticuli'",
                is_verified=True)
    except ValidationError as err:
        e = err.errors()[0]["msg"]
        print(e)
        return

    boom = boom


if __name__ == "__main__":
    main()


"""

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

XXX
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

Custom Validation rules
    -@model_validator(mode=’after’)
        • Contact ID must start with "AC" (Alien Contact)
        • Physical contact reports must be verified
        • Telepathic contact requires at least 3 witnesses
        • Strong signals (> 7.0) should include received messages
"""
