import pwinput
from termcolor import colored
import csv
import os

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    return pwinput.pwinput(prompt)

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    return input(prompt)

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
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not any(char in '!@#$%^&*()' for char in password):
        print("Password must contain at least one special character (!@#$%^&*()).")
        return False
    return True


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) < 3:
        print("Username must be at least 3 characters long.")
        return False
    if not username.isalnum():
        print("Username must only contain letters and numbers.")
        return False
    return True

def save_user_info(username: str, password: str) -> None:
    database_path = "users.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    try:
        with open("users.csv", 'a') as file:
            
           file.write(f"{username},{password}\n")
        print("User information saved successfully!")
    except FileNotFoundError:
        print(f"{database_path} not found")
    

if __name__ == "__main__":
    #use to test the functions
    pass