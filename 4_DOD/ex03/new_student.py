import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A data class that represents a Student

    Attributes:
        name (str):
            name of the student
        surname (str):
            surname of the student
        active (bool):
            active status of the student
        login (str): [non-initializable]
            username of the student generated from their name and surname
        id (str): [non-initializable]
            randomly generated ID of the student
    """

    # initializable attributes
    name: str
    surname: str

    # attributes with defaults
    active: bool = True

    # non-initializable attributes
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    # for attributes that depend on other attributes
    def __post_init__(self):
        """
        Method for post-init processing
        """

        # set the username based on student's name and surname
        self.login = self.name[0] + self.surname
