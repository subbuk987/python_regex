# User Registration Using Regex Validation

A Python-based user registration system that utilizes regular expressions to validate user inputs such as names, email addresses, mobile numbers, and passwords. This project serves as a practical example of input validation in Python.

## Features

- **Name Validation**: Ensures that first and last names start with a capital letter and contain at least three characters.
- **Email Validation**: Validates email addresses against a standard pattern.
- **Mobile Number Validation**: Checks for a valid mobile number format, including country code.
- **Password Validation**: Enforces strong password policies, including length and character requirements.
- **User-Friendly Prompts**: Provides clear instructions and feedback to users during the registration process.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/subbuk987/python_regex.git
   cd python_regex
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install any dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is available only for test branch.*

### Usage

Run the application using the following command:

```bash
python app.py
```

Follow the on-screen prompts to enter your registration details. The application will validate each input and provide feedback accordingly.

## Project Structure

```
python_regex/
├── UserRegistration/
│   └── registration.py  # Contains the User class and validation logic
├── app.py               # Entry point for the application
├── .gitignore           # Specifies files and directories to be ignored by Git
└── README.md            # Project documentation
```

