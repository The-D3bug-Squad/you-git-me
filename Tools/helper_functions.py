import pwinput
import re
from termcolor import colored
import csv

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    prompt = input("Enter your password: ")
    return prompt

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
    if len(username) >= 3 and username != re.search(r'[@!~`-]', username):
        return True
    else:
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
with open('users.csv', mode = 'r') as file:
    csvFile = csv.reader(file)


if __name__ == "__main__":
    #use to test the functions
    pass