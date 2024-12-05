# import the tools
from Tools.helper_functions import*        

def main():
    #implement logic for the program to work correctly use given functions you implemented
    username = get_username("Enter your username: ")
    while username:
        if validate_username(username):
            password = get_password("Enter password: ")
            break
        else:
            print("Invalid username")

    while password:
        if validate_password(password):
            save_user_info(username, password)
            print(colored("USER ADDED SUCCESSFULLY :)", "light_green"))
            break
        else:
            print("Invalid password")


if __name__ == "__main__":
    main()