# import pwinput
# from termcolor import colored
import re

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password() :
    """
    Get a password from the user.
    """
    password=input("Enter your password: ")
    return password

def get_username():
    """
    Get a username from the user.
    """
    username=input("Enter your username: ")
    return username


def validate_password(password):
    """
    Validate a password.
    a valid password should contain:
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character
    """
    special_characters='!@#$%^&*?,./ _'
    has_upper=has_lower=has_number=has_specialchar=False
    if len(password)<8:
        return False
    for i in password:
        if i.isupper():
            has_upper=  True
        elif i.islower():
            has_lower= True
        elif i.isdigit():
            has_number=True
        elif i in special_characters:
            has_specialchar=True
    if has_upper and has_lower and has_number and has_specialchar:
        return True
    
    return False

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username)<3:
        return False
    if re.findall(r'[a-z0-9]',username,re.IGNORECASE):
        return True
    
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