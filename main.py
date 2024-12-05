# import the tools
from Tools.helper_functions import *


def main():
    #implement logic for the program to work correctly use given functions you implemented

    valid_password = get_password("Enter your password: ")
    valid_username = get_username("Enter your username: ")

    if validate_password(valid_password) and validate_username(valid_username):
        save_user_info(valid_username, valid_password)
        print("User information saved successfully.")
    else:
        if not validate_password(valid_password):
            print("Invalid password. Please try again.")
        if not validate_username(valid_username):
            print("Invalid username. Please try again.")
        
if __name__ == "__main__":
    main()
