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
        result = pwinput.pwinput(prompt, mask = "*").strip()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return ""

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        result = input(prompt).strip()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return ""

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
    digit = False
    upper = False
    lower = False 
    special = False

    if len(password) >= 8:
        length = True
    
    for i in password:
        if i.isdigit():
            digit = True
    
    for i in password:
        if i.isupper():
            upper = True
    
    for i in password:
        if i.islower():
            lower = True

    special_characters = "~!@#$%^&*()_+{.}[]|\\:;\"'<,>?-/"
    for i in password:
        if i in special_characters:
            special = True

    return length and digit and upper and lower and special

    
def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) < 3:
        return False
    
    if not username.isalpha():
        return False
    for i in username:
        if i.isdigit():
            return True
    special_characters = "~!@#$%^&*()_+{.}[]|\\:;\"'<,>?-/"
    for i in username:
        if i in special_characters:
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
    user = {username : password}

    if os.path.exists(database_path):
        os.remove(database_path)

    try:
        fieldnames = ["username", "password"]
        with open(database_path,"w", newline=" ") as file:
            file.write(user)
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    #use to test the functions