"""
user_registration.py

This module provides a `User` class that allows user registration with input validation
for names, email, mobile number, and password using regular expressions.

Author: Subramanyam
Date: 2025-04-11
"""

import re


class User:
    """
    A class to collect and validate user registration details.

    Attributes:
        first_name (str): User's first name.
        last_name (str): User's last name.
        _email (str): User's email address.
        _mobile_number (str): User's mobile number.
        _password (str): User's password (stored privately).
    """

    _NAME_PATTERN = re.compile(r'\b[A-Z][A-Za-z]{2,}\b')
    _EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.'
                                r'[A-Za-z]{2,}\b')
    _MOBILE_PATTERN = re.compile(r'\b[1-9][0-9]{0,2}\s[0-9]{10}\b')
    _PASSWORD_PATTERN = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&*^-_><])'
                                   r'.{8,20}$')

    def __init__(self):
        """
        Initializes a User instance with default None values for all fields.
        """
        self.first_name = None
        self.last_name = None
        self._email = None
        self._mobile_number = None
        self._password = None

    def __str__(self):
        """
        Returns a masked string representation of user details.

        Returns:
            str: A formatted string showing user details (password hidden).
        """
        return (f"User Details: \n"
                f"First Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Email: {self._email}\n"
                f"Mobile Number: {self._mobile_number}\n"
                f"Password: ********")

    def _accept_name(self, field):
        """
        Accepts and validates a name input (First or Last).

        Args:
            field (str): Field name (used in prompt, e.g., 'First Name').

        Returns:
            str: Validated name string.
        """
        while True:
            name = input(f"Enter {field}: ").strip()
            if self._NAME_PATTERN.fullmatch(name):
                return name
            print(f"{field} should start with a capital letter "
                  f"and be at least 3 characters long.")

    def _accept_email(self):
        """
        Accepts and validates an email address.

        Returns:
            str: Validated email address.
        """
        while True:
            email = input("Enter Email Address: ")
            if self._EMAIL_PATTERN.fullmatch(email):
                return email
            print("Entered Email Address is NOT valid!")

    def _accept_mobile(self):
        """
        Accepts and validates a mobile number in the format: country_code number.

        Returns:
            str: Validated mobile number.
        """
        while True:
            mobile = input("Enter Mobile Number (e.g., 91 7200920651): ")
            if self._MOBILE_PATTERN.fullmatch(mobile):
                return mobile
            print("Entered Mobile Number is NOT valid!")

    def _accept_password(self):
        """
        Accepts and validates a password with confirmation.

        Password rules:
            - Minimum 8 characters
            - At least one uppercase letter
            - At least one digit
            - At least one special character

        Returns:
            str: Validated password.
        """
        while True:
            password = input("Enter Password: ")
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Passwords do not match!")
                continue
            if self._PASSWORD_PATTERN.fullmatch(password):
                return password
            print("Password Rules:\n"
                  "- At least 8 characters\n"
                  "- At least 1 uppercase letter\n"
                  "- At least 1 digit\n"
                  "- At least 1 special character")

    def register(self):
        """
        Runs the full user registration process.
        Prompts the user to input all necessary fields with validation.
        """
        self.first_name = self._accept_name("First Name")
        self.last_name = self._accept_name("Last Name")
        self._email = self._accept_email()
        self._mobile_number = self._accept_mobile()
        self._password = self._accept_password()
        print("User Registration Successful!")

    def check_email(self,email):
        """
        Used for Checking email outside the class.
        Don't be used in the real Module for abstraction.
        :param email: Email to be checked.
        :return: 1 if passed else -1
        """
        if self._EMAIL_PATTERN.fullmatch(email):
            return 1
        else:
            return -1



if __name__ == "__main__":
    user = User()
    email_list = [
        "abc@yahoo.com",
        "abc-100@yahoo.com",
        "abc.100@yahoo.com",
        "abc111@abc.com",
        "abc-100@abc.net",
        "abc.100@abc.com.au",
        "abc@1.com",
        "abc@gmail.com.com",
        "abc+100@gmail.com"
    ]
    for email_id in email_list:
        if user.check_email(email_id) == 1:
            print("Email is Valid")
        else:
            print("Email is Not Valid")

