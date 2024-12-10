# import the tools
from Tools import helper_functions


def main():
    #implement logic for the program to work correctly use given functions you implemented
    count = 0
    user_password = helper_functions.get_password(input("enter your password: "))
    user_username = helper_functions.get_username(input("enter your username: "))
    while helper_functions.validate_password(user_password)  == False:
        user_password = helper_functions.get_password()
    else:
        count += 1
    while helper_functions.validate_username(user_username) == False:
        user_username = helper_functions.get_username()
    else:
        count += 1

    if count == 2:
        helper_functions.save_user_info(user_username,user_password)

    

if __name__ == "__main__":
    main()