import re

# ****** Username check ******
def username_is_valid(UserName):
    if len(UserName) == 0:
        return False
    if len(UserName) > 50:
        return False
    return True

# ****** Password check ******

def password_is_valid(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


# ****** Email check ******
def email_is_valid(email):
    email_check = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_check, email):
        slicing = email.split('@')
        if len(slicing) == 2:
            sub_slicing, all_slicing = slicing
            if len(sub_slicing) > 0 and len(all_slicing) > 0:
                return True
    return False

def main():
    print("Hello there, write the following details please:")

    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    # ****** Username Validation ******
    if username_is_valid(username):
        print("Username is valid.")
    else:
        print("Username is invalid.")
    

    # ***** Password Validation *****
    if password_is_valid(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")
    

    
    # ***** Email Validation *****
    if email_is_valid(email):
        print("Email is valid.")
    else:
        print("Email is invalid.")

if __name__ == "__main__":
    main()
