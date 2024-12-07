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
    try:
        p = input(prompt)
    except EOFError:
        p = 'securePassword123!'
    finally:
        return p

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    return input(prompt)

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

    validity_code = '0 0 0 0'.split()
    if len(password) < 8:
        return False

    for c in password:
        if c in string.ascii_lowercase:
            validity_code[0] = '1'
        elif c in string.ascii_uppercase:
            validity_code[1] = '1'
        elif c.isdigit():
            validity_code[2] = '1'
        elif c in string.punctuation:
            validity_code[3] = '1'

    if ''.join(validity_code) == '1111':
        return True
    
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
    
    for c in username:
        if c in string.punctuation:
            return False
        
    return True

def save_user_info(username: str, password: str) -> None:
    database_path = "user_data.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    try:
        with open(database_path, 'a') as db:
            
            new_user = {'username':username,
                        'password':password}


            writer = csv.DictWriter(db, fieldnames=['username', 'password'])
            writer.writerow(new_user)
           
                
    except FileNotFoundError:
        raise FileNotFoundError(f"File does not exist check file path: {database_path}")


if __name__ == "__main__":
    #use to test the functions
    pass