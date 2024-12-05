from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info
import time
from termcolor import colored, cprint

def main():
    #implement logic for the program to work correctly use given functions you implemented
    print("Hello, please enter your credentials.")
    username = get_username("Username: ")
    password = get_password("Password: ")
    print("Checking password validity...")
    time.sleep(1)
    if validate_password(password):
        print("Checking username validity...")
        time.sleep(1)
        if validate_username(username):
            print("Adding you to database...")
            time.sleep(1)
            save_user_info(username,password)
    else:
        error = colored("Failed to add to database", "red")
        print(error)

if __name__ == "__main__":
    main()