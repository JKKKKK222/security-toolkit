import string

def check_password_length(password):
    if len(password) >= 8:
        return True
    else:
        return False

def check_has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_has_special(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False