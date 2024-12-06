import pwinput

def get_password(prompt: str) -> str:
    password = pwinput.pwinput(prompt); return password

def get_username(prompt: str) -> str:
    username = input(prompt); return username

def validate_password(password: str) -> bool:
    if len(password) < 8: return False
    has_upper, has_lower, has_digit, has_special = any(char.isupper() for char in password), any(char.islower() for char in password), any(char.isdigit() for char in password), any(not char.isalnum() for char in password)
    return has_upper and has_lower and has_digit and has_special

def validate_username(username: str) -> bool:
    return len(username) >= 3 and username.isalnum()

def save_user_info(username: str, password: str) -> None:
    database_path = "./Database/users.csv"
    with open(database_path, "a") as file: file.write(f"{username},{password}\n")


