# Python User Registration with Regex Validation

A Python-based user registration system that employs regular expressions to validate user inputs such as names, email addresses, mobile numbers, and passwords. This project serves as a practical example of input validation in Python.

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

1. **Clone the repository:**

   ```bash
   git clone https://github.com/subbuk987/UserRegistrationProblem.git
   cd UserRegistrationProblem
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using:

```bash
python app.py
```

Follow the on-screen prompts to enter user details. The application will validate each input and provide feedback accordingly.

## Project Structure

- `app.py`: Main application script that handles user interaction.
- `UserRegistration/registration.py`: Contains the `User` class with validation methods.
- `tests/`: Directory containing test cases for the application.
- `test_data.json`: JSON file containing test data for validation.
- `log_pass.json` & `log_fail.json`: Logs of successful and failed validations, respectively.

## Testing

To run the test suite:

```bash
pytest
```

Ensure that you have the `pytest` framework installed. The tests will validate various user input scenarios and log the outcomes.
