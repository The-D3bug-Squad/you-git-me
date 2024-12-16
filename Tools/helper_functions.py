import pwinput
import re

def get_password(prompt: str) -> str:
    """
    Get a password from the user securely.
    """
    try:
        # Secure password input
        users_password = pwinput.pwinput(prompt)  
        return users_password
    except KeyboardInterrupt:
        # Handle user interruption
        print("\nPassword input interrupted.")
        return ""
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An error occurred: {e}")
        return ""

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    try:
        username = input(prompt)
        return username
    except KeyboardInterrupt:
        print("\nUsername input interrupted.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def validate_password(password: str) -> bool:
    """
    Validate a password.
    A valid password should contain:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[\W_]', password):
        return False
    return True

def validate_username(username: str) -> bool:
    """
    Validate a username.
    A valid username should contain:
    - At least 3 characters
    - Only alphanumeric characters (no special characters)
    """
    if len(username) < 3:
        return False
    if not username.isalnum():
        return False
    return True

def save_user_info(username: str, password: str) -> None:
    """
    Save the user's information to a file.
    Appends the username and password to the file (ensuring no duplicates).
    """
    database_path = "./Database/user_data.csv"
    
    try:
        with open(database_path, "a") as file:
            file.write(f"{username},{password}\n")
    except Exception as e:
        print(f"Error saving user info: {e}")
