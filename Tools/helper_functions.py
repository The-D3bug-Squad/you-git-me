import pwinput
import re
from termcolor import colored
import csv



# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """

    password = pwinput.pwinput(prompt)
    return password


def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    prompt = input("Enter your username: ")
    return prompt

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
    if len(password) >= 8 and re.search(r'[A-Z]',password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[@!~`-]',password) and password.replace(" ", ""):
        return True
    
    else:
        return False
    
database_path = "./Database/users.csv"
   

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) >= 3:
        if re.match(r'^[a-zA-Z0-9]*$', username):  
            return True
    return False
def reader():

    with open(database_path, 'r') as file:
        read_file = csv.reader(file)
        return list(read_file)
    
read_file = reader()

def save_user_info(username: str, password: str) -> None:
   
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    for line in read_file:
        if [username, password] == line:
            msg = colored("Username and password already exists",'red')
            print(msg)
            return
    try:
        with open(database_path, 'a') as file:
            data_info = f"{username},{password}"
            file.write(f"{data_info}\n")
            result = colored("You have been successfully added to the database", "green")
            print(result)

    except Exception as e:
        error_msg = colored(f"Failed to add to database : {e}", 'red')
        print(error_msg)

if __name__ == "__main__":
    #use to test the functions
    #save_user_info('naledi', 'password123')
    pass