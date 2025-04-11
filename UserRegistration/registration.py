# User Registration Module

import re
from exceptions import FormatError


class User:
    _NAME_PATTERN = re.compile(r'\b[A-Z][A-Za-z]{2,}\b')
    _EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self._email = None
        self._mobile_number = None
        self._password = None

    def _accept_name(self, field):
        while True:
            name = input(f"Enter {field}: ").strip()
            if self._NAME_PATTERN.fullmatch(name):
                return name
            else:
                print(
                    f"{field} Should start with a Capital Letter and "
                    f"contain at least 3 characters"
                )

    def _accept_email(self):
        while True:
            email = input("Enter Email Address: ")
            if self._EMAIL_PATTERN.fullmatch(email):
                return email
            else:
                print("Email Address is not valid!!!")

    def create(self):
        self.first_name = self._accept_name("First Name")
        self.last_name = self._accept_name("Last Name")
        self._email = self._accept_email()


if __name__ == "__main__":
    user = User()
    user.create()

