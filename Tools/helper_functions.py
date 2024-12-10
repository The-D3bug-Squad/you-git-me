import pwinput
import termcolor
from csv import writer

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    password = pwinput.pwinput(prompt=prompt)
    return password

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    prompt = input("enter your username: ")
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

    if (len(password) < 8) :
        return False
    
    has_digit = False
    has_upper = False
    has_lower = False
    has_symbol = False


    for character in password:
        if character.islower():
            has_lower = True
        if character.isupper():
            has_upper = True
        if character.isdigit():
            has_digit = True
        if character in "!@#$%&*_-":
            has_symbol = True

    return has_symbol and has_lower and has_digit and has_upper
    #return has_digit
    # return has_lower
        # print(has_symbol)
        # print(has_upper)
print(validate_password("wtdtd125@D"))



def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """

    if (len(username) < 3):
        return False
    has_digit = True
    has_symbol = True

    for character in username:
        if character.isdigit():
            has_digit = False
        if character in  "!@#$%&*_-":
            has_symbol = False

    return has_symbol and has_digit



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
    with open(database_path,"") as f_objects:
        f_objects.write(list) 

        list = [username,password]

        writer_object = writer(f_objects)

        writer_object.writerow(list)

        f_objects.close()

    



if __name__ == "__main__":
    #use to test the functions
    pass