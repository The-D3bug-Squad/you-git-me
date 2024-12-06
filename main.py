# import the tools
from Tools.helper_function.py import *


def main():
    #implement logic for the program to work correctly use given functions you implemented
    username = get_username("Enter your username: ")
    password = get_password("Enter your password: ")
    
    if validate_username(username) and validate_password(password):
        save_user_info(username, password)
    else:
        return ValueError("Invalid username and password!")



if __name__ == "__main__":
    main()
