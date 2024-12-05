import pwinput
from termcolor import colored
import string

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    user_password = pwinput.pwinput(prompt)
    return user_password

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
    Bool = False
    def length():
        if len(password) >= 8:
            return True
        else:
            return False

    def lower():
        for x in password:
            if x.islower():
                return True
            else:
                continue

    def upper():
        for x in password:
            if x.isupper():
                return True
            else:
                continue
        3
    def digit():
        for x in password:
            if x.isdigit():
                return True
            else:
                continue

            
    def special_character():
        for x in password:
            if x in string.punctuation:
                return True
            else:
                continue

    if length() and lower() and upper() and digit() and special_character():
        Bool = True
        return Bool
    else:
        return Bool

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) < 3:
        return False
    elif username.isalnum():
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



if __name__ == "__main__":
    #use to test the functions
    pass