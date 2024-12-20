from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info


def main():
    #implement logic for the program to work correctly use given functions you implemented
    password=get_password("Please enter your password: ")
    while not validate_password(password):
        print("Invalid password, try again!")
        password=get_password("Please enter your password: ")
    print("Password is valid!!")
        
    
    
    username=get_username("Please enter username: ")
    while not validate_username(username):
        print("This username is invalid.Try again!")
        username=get_username("Please enter username: ")
    print(f"Welcome, {username.title()}!")

    save_user_info(username,password)
    print("Saved!")
    



if __name__ == "__main__":
    main()