# import the tools
from Tools.helper_functions import*        

def main():
    #implement logic for the program to work correctly use given functions you implemented
    username = get_username("Enter your username: ")
    password = get_password("Enter password: ")

    execute = 1
    while execute == 1:
        username = get_username("Enter your username: ")
        password = get_password("Enter password: ")
        if validate_password(password) and validate_username(username):
            save_user_info(username, password)
            print(colored("USER ADDED SUCCESSFULLY :)", "light_green"))
            execute -= 1
        else:
            print("Invalid user name or password. Please try again.")



      


if __name__ == "__main__":
    main()