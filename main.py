from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info

def main():
    # Get username from the user
    username = get_username("Enter your username: ")

    # Validate the username
    if not validate_username(username):
        print("Invalid username. Please try again.")
        return  

    # Get password from the user securely
    password = get_password("Enter your password: ")

    # Validate the password
    if not validate_password(password):
        print("Invalid password. Please ensure it meets all criteria.")
        return  

    # Save the user information to a file (only valid data reaches this point)
    save_user_info(username, password)
    print("User information saved successfully!")

if __name__ == "__main__":
    main()
