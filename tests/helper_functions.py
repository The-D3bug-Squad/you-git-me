import pwinput
from termcolor import colored
import string
import csv

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    user_password = pwinput.pwinput(prompt= prompt)
    return user_password

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    user_username = pwinput.pwinput(prompt= prompt)
    return user_username

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
    special_characters = string.punctuation
    valid_pass = False
    
    if len(password) >= 8:
        valid_pass = True

    if valid_pass:
        for character in password:
            if not character.isupper():
                valid_pass = False
            else:
                valid_pass = True
                break
    
    if valid_pass:
        for character in password:
            if not character.islower():
                valid_pass = False
            else:
                valid_pass = True
                break
    
    if valid_pass:
        for character in password:
            if not character.isdigit():
                valid_pass = False
            else:
                valid_pass = True
                break
    
    if valid_pass:
        for character in password:
            if character not in special_characters:
                valid_pass = False
            else:
                valid_pass = True
                break

    return valid_pass

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    viable = True

    if len(username) < 3:
        viable = False
    
    if viable:
        for character in username:
            if not character.isalnum():
                viable = False
                break
    
    return viable


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
    try:
        with open(database_path,'r+') as file:
            file_contents = csv.reader(file)
            headers = ['username','password']
            data = {'username':username,'password':password}
            write_into_file = csv.DictWriter(file,fieldnames=headers)
            write_into_file.writerow(data)
    except FileNotFoundError:
        print("File was not found")

if __name__ == "__main__":
    #use to test the functions
    pass