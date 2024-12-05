import string
import csv
import pwinput
from termcolor import colored

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    password = pwinput.pwinput(prompt = "Enter your password: ", mask = "*")
    
def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    username = pwinput.pwinput(prompt = "Enter your username: ")
    
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
    digits = False
    letters = False
    lowercase = False
    uppercase = False
    special_chars = False
    
    if len(password) >= 8:
        return True
    for i in password:
        if i.isdigit():
            digits = True
        if i.isalpha():
            letters = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
        if i in string.punctuation:
            special_chars = True
    if length and digits and letters and lowercase and uppercase and special_chars:
        return True
    return False 
def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    length = False
    no_alnum = False
    
    if len(username) >= 3:
        length = True
    if username is not username.isalnum():
        no_alnum = True

    if length and no_alnum:
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
    with open(database_path, mode = "a", newline = "") as f:
        writer = csv.writer(f, delimiter = ",")

        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        writer.writerow([username, password])
        
    with open(database_path, mode = "r") as f:
        reader = csv.reader(f, delimiter = ",")

        for row in reader:
            if row == [username, password]:
                return "You're already logged in!"
            


if __name__ == "__main__":
    #use to test the functions
    pass
