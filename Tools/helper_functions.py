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
    try:
        password = pwinput.pwinput(prompt)
        return password
    except ValueError:
        print(colored("Error while reading password", "red"))

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        username = input(prompt)
        return username
    except ValueError:
        print(colored("Error while readig username!", "red"))

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
    pattern =  r"^[a-zA-Z0-9]{3,}$"
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
    # If the file exists and read the existing data
    if os.path.exists("user_data.csv"):
        with open("user_data.csv", "r") as f:
            existing_users = f.readlines()

        # Check if the username and password combination already exists
        for line in existing_users:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                print(colored("This username and password combination already exists!","red"))
                return

    # If no duplicates are found, append the new username and password
    with open("user_data.csv", "a") as f:
        f.write(f"{username},{password}\n")
        print(colored(f"User {username} added successfully!", "green"))


if __name__ == "__main__":
    #use to test the functions
    pass