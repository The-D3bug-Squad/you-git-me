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
        return pwinput.pwinput(prompt=prompt)
    except ValueError:
        pass

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        return input(prompt)
    except ValueError:
        pass

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
    

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    return len(username) >= 3 and username.isalpha()

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

    with open(database_path, "r") as database:
        reader = csv.reader(database)
        existing_usernames = [row[0] for row in reader]

    if username in existing_usernames:
        return f"{username} already exist"
    else:
        with open(database_path, 'a') as data:
            writer = csv.writer(data)
            writer.writerow([username, password])
            return f"{username} added to database"

print(save_user_info("Tshepiso", "id8fu89f"))

if __name__ == "__main__":
    #use to test the functions
    pass