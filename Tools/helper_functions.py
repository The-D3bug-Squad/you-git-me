import pwinput
from termcolor import colored
import csv

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """

    try:
        password = pwinput.pwinput(prompt=prompt)
        return password
    except:
        return 

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        username = input(prompt)
        return username
    except:
        return

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
    if len(password) >= 8:
        upper = 0
        lower = 0
        digit = 0
        special = 0
        for char in password:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdigit():
                digit += 1
            else:
                if char.isalnum():
                    continue
                else:
                    special += 1
        if upper > 0 and lower > 0 and digit > 0 and special > 0:
            return True
        else:
            return False
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
        for char in username:
            if char.isalnum():
                continue
            else:
                return False
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
    try:
        with open(database_path,"a") as file:
            with open(database_path,"r") as f:
                reader = csv.reader(f)
                for line in reader:
                    if [username,password] == line:
                        return "Username and password already exists"
                info = f"{username},{password}"
                file.write(f"{str(info)}\n")
                return "You have been successfully added to the database"
    except:
        return "Failed to add to database"

if __name__ == "__main__":
    #use to test the functions
    pass