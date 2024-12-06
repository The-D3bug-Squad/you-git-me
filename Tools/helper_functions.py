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
    return pwinput.pwinput(prompt, mask = "*")

password = get_password("Enter your password: ")
    
def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    return input(prompt)

username = get_username("Enter your username: ")
    
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
        length = True
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
    no_special_chars = True
    
    if len(username) >= 3:
        length = True
    if username is not username.isalnum():
        no_alnum = True
    for i in username:
        if i in string.punctuation:
            no_special_chars = False

    if length and no_alnum and no_special_chars:
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
    with open(database_path, "a") as f:
        f.seek(0)
        
        reader = csv.reader(f)
        for row in reader:
            if row == [username, password]:
                print("Username already exists")
                
        writer = csv.writer(f) 
        writer.writerow([username, password])
        
if __name__ == "__main__":
    #use to test the functions
    pass
