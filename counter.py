from dataclasses import dataclass
@dataclass
class Urian:
    name: str
    age: str
    course: str

    def nominate(self, student: "Urian") -> None:
        self._set_student_profile(student)

    def _set_student_profile(self, student: "Urian") -> None:
        pass