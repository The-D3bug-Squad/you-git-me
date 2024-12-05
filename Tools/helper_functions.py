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
    password = pwinput.pwinput(prompt, mask="*")
    return password
    

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """

    username = input(prompt)
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
                                    
    char = string.punctuation
    upper_cnt, lower_cnt, digit_cnt, char_cnt = 0, 0, 0, 0 
    
    if len(password) > 8:
        for i in range(len(password)):
            if password[i].isupper():
                upper_cnt = 1   
            if password[i].islower():
                lower_cnt = 1  
            if password[i].isdigit():
                digit_cnt = 1   
            if password[i] in char:
                char_cnt = 1
    if upper_cnt + lower_cnt + digit_cnt + char_cnt == 4:
        return True
    else:
        return False 
                                    

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    if len(username) >= 3 and username.isalnum():
        return True
    else:
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
    try:
        with open(database_path, mode="r") as file:
            database = csv.reader(file)
            
            if username in database and password in database:
                raise colored("User already exists", "red")
            else:
                with open(database_path, mode="w") as file:
                    database = csv.writer(file)
                    database.writerow(f"{username}, {password}")

    except FileNotFoundError:
        print(colored("File not found", "red"))



if __name__ == "__main__":
    #use to test the functions
    # save_user_info(get_username("Enter username"), get_password("Enter password: "))
    pass