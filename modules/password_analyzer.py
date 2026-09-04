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

def calculate_score(password):
    score = 0
    if check_password_length(password):
        score += 1
    if check_has_digit(password):
            score += 1
    if check_has_uppercase(password):
            score += 1
    if check_has_lowercase(password):
            score += 1
    if check_has_special(password):
            score += 1
    return score

def get_strength(password):
    score=calculate_score(password)
    if score <= 2:
        return "Weak"
    elif score == 5:
        return "Strong"
    else:
        return "Medium"