import pwinput
from termcolor import colored, cprint
import csv

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """

    password = pwinput.pwinput(prompt=prompt)
    return password

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
    length = len(password) < 8
    lower = password.islower()
    upper = password.isupper()
    alnum = password.isalnum()

    validation = not length and not lower and not upper and not alnum

    match validation:
        case True:
            digit = 0
            for char in password:
                if char.isdigit():
                    digit += 1
            return digit > 0
        case False:
            return False
    


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """

    length = len(username) >= 3
    alnum = username.isalnum()
    validation = (length and alnum) == True
    match validation:
        case True:
            return True
        case False:
            return False
    
database_path = "./Database/users.csv"

def get_reader():
    try:
        with open(database_path, "r") as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        error = colored(f"Failed to get data from database", "red")
        print(error)
        return

reader = get_reader()

def save_user_info(username: str, password: str) -> None:
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    for line in reader:
        if [username,password] == line:
            message = colored("Username and password already exists", "red")
            print(message)
            return
        
    try:
        with open(database_path,"a") as file:
            info = f"{username},{password}"
            file.write(f"{info}\n")
            result = colored("You have been successfully added to the database", "green")
            print(result)
    except FileNotFoundError:
        error = colored(f"Failed to add to database", "red")
        print(error)

if __name__ == "__main__":
    #use to test the functions
    pass