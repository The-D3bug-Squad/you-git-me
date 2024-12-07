# import the tools
from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info
from termcolor import colored, cprint


def main():
    #implement logic for the program to work correctly use given functions you implemented
    try:
        print("Hello, please enter your credentials.")
        
        username = get_username("Username: ")
        password = get_password("Password: ")
        
        print("Checking password and username is validity. please wait abit.")
        
        if not validate_username(username) or not validate_password(password):
            raise ValueError(colored("Invalid username or password", "red"))
        
        print("Adding you to the server database.")
        
        save_user_info(username, password)
        
    except Exception as e:
        error_message = colored(f"An unexpected error occurred: {e}", "red")
        print(error_message)

if __name__ == "__main__":
    main()