import pwinput
from termcolor import colored

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    try: 
        password = pwinput.pwinput(prompt)
        return password
    except:
        print(colored("Invalid input", "red"))


def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """

    try: 
        username = input(prompt)
        return username
    except:
        print(colored("Invalid input", "red"))


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
    valid_length = len(password) >= 8
    upper_case = any(char.isupper() for char in password)
    lower_case = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char.isalnum() for char in password)

    return valid_length and upper_case and lower_case and digit and special_char


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    
    return len(username) >= 3 and not any(char.isalnum() for char in username)
    

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
        with open(database_path, "a") as file:
            file.write(f"{username},{password}\n")
    except:
        print(colored("Could not save user information", "red"))

if __name__ == "__main__":
    #use to test the functions
    pass