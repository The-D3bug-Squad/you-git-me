import pwinput
from termcolor import colored
import re
import os

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int


def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    password = pwinput.pwinput(prompt)
    return password


def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    username = input(prompt)
    return username


def validate_password(password: str) -> bool:
    """
    Validate a password.
    a valid password should contain:
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\"#$%&\'()*+,\-.\/:;<=>?@\[\\\]^_`{|}~!])(.{8,})$"
    if re.match(pattern, password):
        return True
    return False


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    pattern = r"^[a-zA-Z0-9]{3,}$"
    if re.match(pattern, username):
        return True
    return False


def save_user_info(username: str, password: str) -> None:
    database_path = "./Database/users.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    if os.path.exists(database_path):
        with open(database_path, "r") as file:
            existing_users = file.readlines()
        
        for user in existing_users:
            if username in user:
                print(colored("This user already exists!", "red"))
                return
    with open(database_path, "a") as file:
        file.write(f"{username},{password}\n")


if __name__ == "__main__":
    # use to test the functions
    pass
