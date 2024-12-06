# import the tools
from Tools.helper_functions import *


def main():
    #implement logic for the program to work correctly use given functions you implemented
    print("User authantication utility\n\n")
    input(f"Press enter to create a user.\n\n")

    username = ""
    password = ""

    while not validate_username(username):
        username = get_username("Enter username: ")
        print()
        if not validate_username(username):
            print("Username must have atleast 3 alphanumeric characters.")
    
    while not validate_password(password):
        password = get_password("Enter password: ")
        print()
        if not validate_password(password):
            print(""" a valid password should contain:
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character\n""")
        
    if validate_password(password) and validate_username(username):
        save_user_info(username,password)
        print("User info sucessfully saved.\n")

if __name__ == "__main__":
    main()