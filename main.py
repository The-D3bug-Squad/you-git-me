from Tools.user_functions import *

def main():
    password_input = get_password("Enter your password: ");
    username_input = get_username("Enter your username: ");
    if validate_password(password_input) and validate_username(username_input): save_user_info(username_input, password_input);
    else:
        if not validate_password(password_input): print("Invalid password. Please try again.");
        if not validate_username(username_input): print("Either username already exists or username is invalid. Please try again.");
        
if __name__ == "__main__":
    main()