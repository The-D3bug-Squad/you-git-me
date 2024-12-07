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
    try:
        return pwinput.pwinput(prompt = prompt)
    except TypeError:
        return "Please enter correct input"

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        return input(prompt)
    except TypeError:
        return "Please enter the username"

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
    length = False
    number = False
    upper_case = False
    lower_case = False
    special = False
    try:
        if len(password) >= 8:
            length = True
            for letter in password:
                    if letter.isdigit():
                        number = True
                    if letter.isupper():
                        upper_case = True
                    if letter.islower():
                        lower_case = True 
                    if letter in "!, @, #, $, %, ^, &, *, (, ), _, +, =, {, },, |, ;, :, \", ', <, >, /, ?":
                        special = True
        else:
            return False
        return length and number and lower_case and upper_case and special
    except TypeError:
        return "Enter a password"


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    try:
        return len(username) >= 3 and username.isalpha()
    except TypeError:
        return "Please enter username"

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
        with open(database_path, "a") as data:
            data.write(f"{username},{password}\n")
            print(f"{username} added to database")

    except FileNotFoundError:
        print(f"{database_path} not found")

if __name__ == "__main__":
    #use to test the functions
    pass