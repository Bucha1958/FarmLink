#!/usr/bin/python3
from models import storage
from models.farmer import Farmer
from models.base_model import BaseModel, Base
from werkzeug.security import generate_password_hash, check_password_hash


def test_password_hashing():
    # Get the password from the user during registration
    user = storage.get(Farmer, 'a44daf8c-8a55-4b14-b356-90cc0dee7f27')
    print(user)
    password = input("Enter password: ")

    # Hash the password
    hashed_password = generate_password_hash(password)

    print("Hashed Password:", hashed_password)

    # Get the password from the user during authentication
    login_password = input("Enter login password: ")

    # Verify the password
    if check_password_hash(hashed_password.strip(), login_password.strip()):
        print("Authentication successful")
    else:
        print("Authentication failed")

if __name__ == '__main__':
    test_password_hashing()