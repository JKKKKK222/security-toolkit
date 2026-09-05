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

def check_common_password(password):
    weak_password = ["123456", "password", "qwerty", "admin123"]
    if password in weak_password:
        return True
    return False

def check_not_common_password(password):
    return not check_common_password(password)

def check_simple_sequence(password):
    for i in range(len(password) - 2):
        if password[i:i+3].isdigit() or password[i:i+3].isalpha():
            diff1 = ord(password[i+2]) - ord(password[i+1])
            diff2 = ord(password[i+1]) - ord(password[i])
            if (diff1 == 1 and diff2 == 1) or (diff1 == -1 and diff2 == -1):
                return True
    return False

def check_no_simple_sequence(password):
    return not check_simple_sequence(password)
    
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
    if check_common_password(password):
        return "Weak"
    score = calculate_score(password)
    if score <= 2:
        return "Weak"
    elif score == 5:
        if check_simple_sequence(password):
            return "Medium"
        return "Strong"
    else:
        return "Medium"

def get_password_feedback(password):
    if check_common_password(password):
        return "该密码属于常见弱密码，即使字符组成复杂，也不建议使用。"
    return "未发现常见弱密码风险。"