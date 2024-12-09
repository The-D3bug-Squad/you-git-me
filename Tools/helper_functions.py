import pwinput
import re
import string
# from termcolor import colored


# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    return pwinput.pwinput(prompt)

    
    
def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    return input(prompt)

def validate_password(password: str) -> bool:
    """
    Validate a password.
    a valid password should contain:
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character
    """
    return True if len(password) >= 8 and  re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('[0-9]', password) and re.search(f'[{string.punctuation}]', password) else False
    # if len(password) < 8:
    #     return False
    # else:
    #     if re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('[0-9]', password) and re.search(f'[{string.punctuation}]', password):
    #         return True
    # return False
# print(validate_password('Password12'))
# print(re.search(f'[{string.punctuation}]','Pa!ssword12'))
# # print(list(string.punctuation))
def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    
    return True if len(username) >= 3 and not re.search(f'[{string.punctuation}]',username) else False

def save_user_info(username: str, password: str) -> None:
    database_path = "./Database/users.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """
    with open(database_path, mode='r') as file:
        content = file.readlines()
        boolean = True
        if boolean:
            for userdetail in content:
                # print(userdetail.split(','))
                if username in userdetail.split(','):
                    boolean = False
        else:
            with open(database_path, mode = 'a') as file:
                file.writelines(f'\n{username},{password}')
                
            
        # if username not in content:
        #     # return False
        #     with open(database_path, mode = 'a') as file:
        #         file.write(f'\n{username},{password}')
        #         # file.close
    return content,username
print(save_user_info('hello', 'passworddd'))

if __name__ == "__main__":
    #use to test the functions
    pass