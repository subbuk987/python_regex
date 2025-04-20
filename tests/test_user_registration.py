import pytest
import json
from datetime import datetime
from UserRegistration.registration import User
from generate_test_data import generate_data

# ---------------------------------
# Global Counters
# ---------------------------------
total_pass = 0
total_fail = 0


# ---------------------------------
# Fixtures
# ---------------------------------
@pytest.fixture(scope="session")
def organize():
    # Clean up the log files before starting
    for file in ("log_pass.json", "log_fail.json"):
        with open(file, "w") as f:
            json.dump([], f)

    # Generate data (if required)
    generate_data()  # Generates and stores the test data in test_data.json

    # Load test data from file
    with open("test_data.json") as f:
        data = json.load(f)

    # Return the User instance and test data
    return (User(), data)


# ---------------------------------
# Parametrized Test
# ---------------------------------
@pytest.mark.parametrize("entry_index", range(1000))
def test_user_validation(organize, entry_index):
    global total_pass, total_fail

    # Extract user instance and data from the fixture
    user_instance, data = organize

    # Fetch the test data for the current entry index
    user_data = data[entry_index]

    # Validate the user data
    result = user_instance.validate_all_fields(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["mobile"],
        user_data["password"]
    )

    # Prepare log entry with required fields: time, result, and user details
    log_entry = {
        "time": datetime.now().isoformat(),
        "result": "PASS" if result else "FAIL",
        "user_details": {
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "email": user_data["email"],
            "mobile": user_data["mobile"]
        }
    }

    # Update the corresponding log file
    log_file = "log_pass.json" if result else "log_fail.json"

    # Read the existing logs
    with open(log_file, "r") as f:
        log_contents = json.load(f)

    # Append the new log entry
    log_contents.append(log_entry)

    # Write the updated log back to the file
    with open(log_file, "w") as f:
        json.dump(log_contents, f, indent=4)

    # Update counters
    if result:
        total_pass += 1
    else:
        total_fail += 1

    # Ensure the test passes or fails as expected
    assert result


