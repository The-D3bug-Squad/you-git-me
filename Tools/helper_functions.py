import pwinput
from termcolor import colored


# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    password = pwinput.pwinput(prompt)
    return password
    

def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    username = input(prompt)
    return username

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
    length = False
    if len(password) >= 8:
      length = True

    upperCase=0
    lowerCase=0
    number=0
    specialCharacter=0

    special_characters="!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~-"
    for i in password:
         if i.isdigit():
            number +=1
         elif i.islower():
            lowerCase += 1
         elif i.isupper():
            upperCase += 1
         elif i in special_characters:
               specialCharacter+=1

    if length and number>=1 and lowerCase>=1 and upperCase>=1 and specialCharacter>=1:
            return True
      
    return False


def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
    
    if len(username) < 3:
        return False

    # for char in username:
    elif not username.isalnum():
        return False
        
    else:
        return True

    
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
    with open('user_data.csv', 'a')as csv_files:
        csv_files.write(f"{username},{password}\n")
    # with open('./Database/users.csv','w')as csv_files:
    #     csv_writer=csv_writer(csv_files)

    #     for users in csv_files:
    #         if username not in csv_files:
    #             csv_files.append(username)
    #         if password not in csv_files:
    #             csv_files.append(password)
        







if __name__ == "__main__":
    #use to test the functions
    pass