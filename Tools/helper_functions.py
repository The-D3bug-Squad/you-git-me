import pwinput
from termcolor import colored
import re
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
    prompt = input('Enter your username: ')
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

    if len(password) >= 8 and re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[0-9]',password) and re.search(r'[@!~`-]',password):
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
        if re.match(r'^[a-zA-Z0-9]*$',username):
            return True
        return False
    
def file_reader():

    with open(database_path, 'r') as f:
        read_file = csv.file_reader(f)
        return list(read_file)
    
read_file = file_reader()   
            

def save_user_info(username: str, password: str) -> None:
 
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    for text in read_file:
        if [username, password] == text:
            message = colored('This username and password already exists.','red')
            print(message)
            return

    try:
        with open(database_path,'a') as f:
            data_details = f'{username},{password}'
            f.write(f'{data_details}\n')
            res = colored('Congratulations! Your details have been successfully added to the user database!') 
            print(res)

    except Exception as e:
        error_text = colored(f'Could not add to user database: {e}', 'red')
        print(res)           

if __name__ == "__main__":
    #use to test the functions
    #save_user_info('Tshegofatso','password000')
    pass