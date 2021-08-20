# 06. Password Validator
def password_validator(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    if len([x for x in password if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


user_password = input()
result = password_validator(user_password)

if result:
    print("Password is valid")