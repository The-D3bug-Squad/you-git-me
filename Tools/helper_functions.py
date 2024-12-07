import pwinput
# from termcolor import colored

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
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False

    if len(password) < 8:
        return False
    for char in password:
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
        if char.isdigit():
            hasDigit = True
        if not any([char.isupper(), char.islower(), char.isdigit()]):
            hasSpecial = True

    return hasUpper and hasLower and hasDigit and hasSpecial


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
   
    if len(username) < 3:
        return False
    
    
    for char in username:
        if char.isalnum() == False: 
            return False
    
    
    return True

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
    with open(database_path, "a") as file:
        file.write(f"{username},{password}\n")

if __name__ == "__main__":
    #use to test the functions
    pass