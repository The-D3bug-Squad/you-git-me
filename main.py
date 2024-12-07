from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info


def main():
    #implement logic for the program to work correctly use given functions you implemented
    name = get_username("Enter your username: ")
    password = get_password("Enter your password: ")

    #Validating username, password and saving them to our database
    if validate_username(name) and validate_password(password):
        save_user_info(name, password)
    else:
        print("Enter a proper username or a strong password")

if __name__ == "__main__":
    main()