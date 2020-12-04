import re
from typing import List, Dict, Optional

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

RULES = {
    "byr": r"^19[2-9]\d|200[0-2]$",
    "iyr": r"^20(1\d|20)$",
    "eyr": r"^20(2\d|30)$",
    "hgt": r"^((1([5-8]\d|9[0-3])cm)|((59|6\d|7[0-6])in))$",
    "hcl": r"^#[A-Fa-f0-9]{6}|$",
    "ecl": r"amb|blu|brn|gry|grn|hzl|oth",
    "pid": r"^\d{9}$",
    "cid": r"",  # Let anything pass
}


class Passport:
    """Stores data and functions for passports."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.fields = self._get_fields()

    def _get_fields(self) -> Dict[str, str]:
        """Gets a dict of all fields in the passport."""
        field_list = self.text.split()
        return dict(field.split(":") for field in field_list)

    def is_valid(self,
                 required_fields: [List[str]],
                 rules: Optional[List[str]] = None) -> bool:
        """Checks if the passport is valid. An optional dict of rules for the fields to follow may be provided."""
        if all(field in self.fields.keys() for field in required_fields):
            if not rules:
                return True
            return all(
                re.match(rules[key], val) for key, val in self.fields.items()
            )

        return False
