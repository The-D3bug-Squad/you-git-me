import pwinput
from termcolor import colored
import string
# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    password=pwinput.pwinput(prompt)
    return password

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    username =input(prompt)
    return username 

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
    uppercase=0
    lowercase=0
    digit=0
    special=0

    if len(password)<8:
        return False
    
    for i in password:
        if i.isupper():
            uppercase += 1
    if uppercase==0:
        return False
        
    for i in password:
        if i.islower():
            lowercase += 1
    if lowercase==0:
        return False
        
    for i in password:
        if i.isdigit():
            digit+=1
    if digit==0:
        return False
    
    for i in password:
        if i in string.punctuation:
            special+=1
    if special==0:
        return False
    return True  

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    count=0
    if len(username)<=3 :
        return False
        # for i in username:
    elif not username.isalnum():
        return False
        # else:
        #     return True
    else:
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

    with open('user_data.csv', 'a') as f:
        f.write('user123,Password123!\n')
# f.write(username,password)

if __name__ == "__main__":
    #use to test the functions
    print(validate_username("user2"))