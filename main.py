from Tools.helper_functions import (
    get_password,
    get_username,
    validate_password,
    validate_username,
    save_user_info,
)
from termcolor import colored


banner = r"""
                   ,,,, 
             ,;) .';;;;',
 ;;,,_,-.-.,;;'_,|I\;;;/),,_
  `';;/:|:);{ ;;;|| \;/ /;;;\__
      L;/-';/ \;;\',/;\/;;;.') \
      .:`''` - \;;'.__/;;;/  . _'-._ 
    .'/   \     \;;;;;;/.'_7:.  '). \_
  .''/     | '._ );}{;//.'    '-:  '.,L
.'. /       \  ( |;;;/_/         \._./;\   _,
 . /        |\ ( /;;/_/             ';;;\,;;_,
. /         )__(/;;/_/                (;;'''''
 /        _;:':;;;;:';-._             );
/        /   \  `'`   --.'-._         \/
       .'     '.  ,'         '-,
      /    /   r--,..__       '.\
    .'    '  .'        '--._     ]
    (     :.(;>        _ .' '- ;/
    |      /:;(    ,_.';(   __.'
     '- -'"|;:/    (;;;;-'--'
           |;/      ;;(
           ''      /;;|
                   \;;|
██████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗     ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ 
██╔══██╗╚════██╗██╔══██╗██║   ██║██╔════╝     ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗
██║  ██║ █████╔╝██████╔╝██║   ██║██║  ███╗    ███████╗██║   ██║██║   ██║███████║██║  ██║
██║  ██║ ╚═══██╗██╔══██╗██║   ██║██║   ██║    ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║
██████╔╝██████╔╝██████╔╝╚██████╔╝╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝
╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝     ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝                                                                                                                      "         
"""


# Define custom username and password errrors.
class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


def main():
    # implement logic for the program to work correctly use given functions you implemented
    print(banner)
    print("Welcome to the D3bug Squad Program!")
    # Validate username
    while True:
        try:
            username = get_username("Enter your username: ")
            if not validate_username(username):
                raise InvalidUsernameError(
                    colored(
                        f"Username error: Username must have alphabets, numbers, no punctuation, and be at least 3 characters long.",
                        "red",
                    )
                )
            break  # Username is valid, exit the loop
        except InvalidUsernameError as e:
            print(e)  # Print the error and ask for the username again

    # Validate password
    while True:
        try:
            password = get_password("Enter your password: ")
            if not validate_password(password):
                raise InvalidPasswordError(
                    colored(
                        f"Password error: Password must be 8 characters long, contain one uppercase and lowercase letter, one digit, and one special character.",
                        "red",
                    )
                )
            break  # Password is valid, exit the loop
        except InvalidPasswordError as e:
            print(e)

    # Save user to database
    save_user_info(username, password)
    print(colored("Thank you for using the program, go write some kode!", "blue"))


if __name__ == "__main__":
    main()
