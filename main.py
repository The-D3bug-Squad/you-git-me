# import the tools
from Tools.helper_functions import *
from termcolor import colored

def main():
    #implement logic for the program to work correctly use given functions you implemented
    try:

        valid_password = get_password("Enter your password: ")
        valid_username = get_username("Enter your username: ")

        if validate_password(valid_password) and validate_username(valid_username):
            save_user_info(valid_username, valid_password)
            print(colored("User information saved successfully.", "green"))
        else:
            if not validate_password(valid_password):
                print(colored("Invalid password. Please try again.", "red"))
            if not validate_username(valid_username):
                print(colored("Invalid username. Please try again.", "red"))
    except:

        print(colored("An error occurred. Please try again.", "red"))

        
if __name__ == "__main__":
    main()
