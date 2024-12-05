# import the tools
from Tools.helper_functions import *


def main():
    #implement logic for the program to work correctly use given functions you implemented
    username  = get_username('Enter your user name: ')
    password = get_password('Enter your password: ')
    if validate_username(username) and validate_password(password):
        save_user_info(username,password)
    else:
        return "Invalid password"




if __name__ == "__main__":
    main()

