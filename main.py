from modules.password_analyzer import check_password_length, check_has_digit, check_has_uppercase, check_has_lowercase, check_has_special
password = input("请输入一个密码：")
result_length = check_password_length(password)
if result_length:
    print("密码长度符合基本要求。")
else:
    print("密码长度过短，建议至少使用 8 个字符。")

result_has_digit = check_has_digit(password)
if result_has_digit:
    print("密码中包含数字字符")
else:
    print("密码中不包含数字字符")

result_has_uppercase = check_has_uppercase(password)
if result_has_uppercase:
    print("密码中包含大写字母")
else:
    print("密码中不包含大写字母")

result_has_lowercase = check_has_lowercase(password)
if result_has_lowercase:
    print("密码中包含小写字母")
else:
    print("密码中不包含小写字母")

result_has_special = check_has_special(password)
if result_has_special:
    print("密码中包含特殊字符")
else:
    print("密码中不包含特殊字符")