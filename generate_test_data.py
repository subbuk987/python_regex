# generate_test_data.py
import random
from faker import Faker
import json

fake = Faker()


def generate_data():
    test_data = []

    for _ in range(1000):
        # Randomly decide if the test should pass or fail
        is_pass = random.choice([True, False])

        if is_pass:
            # Generate valid data
            data = {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "mobile": f"{random.randint(10, 999)} {fake.random_number(digits=10)}",
                "password": fake.password(length=12, special_chars=True,
                                          digits=True, upper_case=True)
            }
        else:
            # Generate invalid data by tweaking one field
            data = {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email() if random.random() > 0.5 else fake.word() + "@example.com",
                # invalid email
                "mobile": f"123 {fake.random_number(digits=9)}",
                # invalid mobile
                "password": fake.password(length=5)
                # invalid password (too short)
            }

        test_data.append(data)

    # Save the test data to a file
    with open("test_data.json", "w") as f:
        json.dump(test_data, f, indent=4)
