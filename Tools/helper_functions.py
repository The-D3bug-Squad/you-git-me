import pwinput
from termcolor import colored
import csv
import os

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    return pwinput.pwinput(prompt)

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
    special_characters = "!@#$%^&*(/)[]}{:;‘’~_|-+=<>?,"

    if len(password) < 8:
        print(colored("Password must be at least 8 characters long", "red"))
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_character = False


    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special_character = True

    if not (has_upper and has_lower and has_digit and has_special_character):
        print(colored("Password must include uppercase, lowercase, digit and special character", "red"))
        return False
    
    return True
        

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    special_characters = "!@#$%^&*(/)[]}{/:;‘~_|-+=<>?,"

    if len(username) < 3:
        print(colored("Username must be at least 3 characters long", "red"))
        return False
    
    for char in username:
        if char in special_characters:
            print(colored("Username must not include any of the special characters", "red"))
            return False
    
    return True


def save_user_info(username: str, password: str) -> None:
    test_file = "./Database/users.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    try:
        if not os.path.exists(test_file):
            with open(test_file, mode="a", newline=" ") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(f"{username},{password}")
                print(colored("Username and password saved succesfully", "green"))

        else:
            with open(test_file, mode="r", newline=" ") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[0] == username:
                        print(colored("Username already exists", "red"))
                        return
    except Exception as e:
        print(colored(f"An error accured while saving the user information: {e}", "red"))


if __name__ == "__main__":
    #use to test the functions
    try:
        username = input("Enter your username: ")
        if not validate_username(username):
            raise ValueError("Incorrect username. Please try again")

        password = pwinput.pwinput("Enter your password: ")
        if not validate_password(password):
            raise ValueError("Incorrect password. Please try again")
        
        save_user_info(username, password)
    except Exception as e:
        print(colored(f"Error: {e}", "red"))
    