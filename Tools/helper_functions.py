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
    if len(password) < 8:
        return False
    
    for i in password:
        if not i.isdigit():
            return False
    
    for i in password:
        if not i.isupper():
            return False
    
    for i in password:
        if not i.islower():
            return False

    special_characters = "~!@#$%^&*()_+{.}[]|\\:;\"'<,>?-/"
    space = [" "]
    for i in password:
        if not i in special_characters or i not in space:
            return False
    
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
    username = get_username()
    password = get_password()

    user = {username : password}

    if os.path.exists(database_path):
        os.remove(database_path)

    try:
        with open(database_path,"a", newline=" ") as file:
            writer = csv.DictWriter(file)
            writer.writerow(user)
    except Exception as e:
        print(f"Errir: {e}")
        return 


if __name__ == "__main__":
    #use to test the functions
    