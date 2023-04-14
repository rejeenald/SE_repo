from dataclasses import dataclass
@dataclass
class Urian:
    name: str
    age: str
    course: str

    def nominate(self, other_urian: "Urian") -> None:
        pass