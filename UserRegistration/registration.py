# User Registration Module

import re
from exceptions import FormatError


class User:
    _NAME_PATTERN = re.compile(r'\b[A-Z][A-Za-z]{2,}\b')

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self._email = None
        self._mobile_number = None
        self._password = None


    def accept_first_name(self, first_name):
        if not self._NAME_PATTERN.fullmatch(first_name):
            print(
                FormatError().msg,
                "First Name Should Start with a Capital Letter "
                "and be at least 3 characters."
            )
        else:
            self.first_name = first_name

    def create(self):
        first_name = input("Enter First Name: ").strip()
        self.accept_first_name(first_name)

if __name__ == "__main__":
    user = User()
    user.create()
    print(user.first_name)
