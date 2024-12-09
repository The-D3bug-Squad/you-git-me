import pwinput
# from termcolor import colored

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    return pwinput.pwinput(prompt, mask='*')

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
    upper = False
    lower = False
    digit = False
    special = False
    if len(password) >= 8:
        for x in password:
            if x.isupper():
                upper = True
            if x.isdigit():
                digit = True
            if x.islower():
                lower = True
            if not any([x.isalpha(), x.isdigit(), x == ' ']):
                special = True
        return upper and lower and digit and special
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
    for x in username:
        if x.isalnum():
            continue
        else:
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
    with open(database_path, 'a') as f:
        
        f.write(f'{username},{password}\n')
        


if __name__ == "__main__":
    #use to test the functions
   pass 