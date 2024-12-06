import pwinput
import re
from termcolor import colored
import csv
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
    prompt = input("Enter your username: ")
    return prompt

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
    if len(password) >= 8 and re.search(r'[A-Z]',password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[@!~`-]',password) and password.replace(" ", ""):
        return True
    
    else:
        return False
def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) >= 3:
        if re.match(r'^[a-zA-Z0-9]*$', username):  
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
   # Ensure the database directory exists
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    
    # Check for duplicates
    exists = False
    if os.path.isfile(database_path):
        with open(database_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:  # Assuming username is in the first column
                    exists = True
                    break
    
    if exists:
        print("Username already exists.")
        return
    
    # Append new user info if no duplicates found
    with open(database_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])  # Save username and password


if __name__ == "__main__":
    #use to test the functions
    pass