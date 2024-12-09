# import the tools
from Tools.helper_functions import get_username, get_password, validate_username, validate_password, save_user_info


def main():
    #implement logic for the program to work correctly use given functions you implemented
        username = get_username("Enter your username: ")
        while not validate_username(username):
              print("Invalid username.")
              username = get_username("Enter your username: ")

        password = get_password("Enter your password: ")
        while not validate_password(password):
              print("Invalid password.")
              password = get_password("Enter your password: ")
        
        save_user_info(username, password)
        print("User information was succesfully saved")

if __name__ == "__main__":
    main()