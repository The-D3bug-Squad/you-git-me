# import the tools
from Tools.helper_functions import (
    get_password,
    get_username,
    validate_password,
    validate_username,
    save_user_info,
)


def main():
    # implement logic for the program to work correctly use given functions you implemented
    username = get_username("Enter your username: ")
    if not validate_username(username):
        print("Invalid username.")
        return
    
    password = get_password("Enter your password: ")
    if not validate_password(password):
        print("Invalid password.")
        return
    
    save_user_info(username, password)


if __name__ == "__main__":
    main()
