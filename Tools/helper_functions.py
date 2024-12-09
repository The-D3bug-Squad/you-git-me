import pwinput
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
        password = pwinput.pwinput(prompt, mask="*")
        return password   
    except ValueError:
        print(colored("Please enter a valid password", "red"))
        return get_password(prompt)

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        username = input(prompt)
        return username
   
    except ValueError:
        print(colored("Please enter a valid username", "red"))
        return get_username(prompt)

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

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_characters = "!@#$%^&*()-+"
    if not any(char in special_characters for char in password):
        return False

    return True

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """

    if len(username) < 3:
        return False

    if not username.isalnum():
        return False

    return True

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
        return input(prompt)
    except ValueError:
        print("Input ended unexpectedly. Please try again.")
        return None

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
    symbol = ["!","@","#","$","%","^","&","*","_","-","/","?","<",">","~"]
    try:
        if len(password) >= 8 and any(chars.isupper() for chars in password) and any(chars.islower() for chars in password) and any(chars.isdigit() for chars in password) and any(chars in symbol for chars in password):
            return True
        else:
            return False
    except TypeError:
        print("Your password is not validate")
        return False


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    try:
        if len(username) >= 3 and username.isalnum():
            return True
        else:
            return False
    except AttributeError:
        print("Invalid input: Username must be a string.")
        return False
            
database_path = 'user_data.csv'

def get_reader():
    
    try:
        with open(database_path, "r") as f:
            reader = csv.reader(f)
            return list(reader)
        
    except Exception as e:
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
            file.write(f"{info}\r\n")
            result = colored("You have been successfully added to the database", "green")
            print(result)
            
    except Exception as e:
        error = colored(f"Failed to add to database : {e}", "red")
        print(error)

if __name__ == "__main__":
    #use to test the functions
    save_user_info("user18", "Password18!")