
import re
def get_password():
    password=input("Enter your password: ")
    return password
security=get_password()

def get_username():
    username=input("Enter your username: ")
    return username
usersname=get_username()

def validate_password(security):
    special_characters='!@#$%^&*?,./ _'
    has_upper=has_lower=has_number=has_specialchar=False
    if len(security)<8:
        return False
    for i in security:
        if i.isupper():
            has_upper=  True
        elif i.islower():
            has_lower= True
        elif i.isdigit():
            has_number=True
        elif i in special_characters:
            has_specialchar=True
    if has_upper and has_lower and has_number and has_specialchar:
        return True
    
    return False

def validate_username(usersname):
    if len(usersname)<4:
        return False
    if re.findall(r'[a-z0-9]',usersname,re.IGNORECASE):
        return True
    
    



    
    
    

def main():
    #implement logic for the program to work correctly use given functions you implemented
    pass



if __name__ == "__main__":
    main()