from modules.password_analyzer import (
    check_password_length, 
    check_has_digit, 
    check_has_uppercase, 
    check_has_lowercase, 
    check_has_special, 
    calculate_score, 
    get_strength, 
    check_not_common_password, 
    get_password_feedback,
    check_no_simple_sequence,
)

password = input("请输入一个密码：")

def display_result(result, success_message, failure_message):
    if result:
        print(success_message)
    else:
        print(failure_message)

checks = [
    (check_password_length,
     "密码长度符合基本要求。",
     "密码长度过短，建议至少使用 8 个字符。"
     ),
    (check_has_digit,
     "密码中包含数字字符",
     "密码中不包含数字字符"
     ),
    (check_has_uppercase,
     "密码中包含大写字母",
     "密码中不包含大写字母"
     ),
    (check_has_lowercase,
     "密码中包含小写字母",
     "密码中不包含小写字母"
     ),
    (check_has_special,
     "密码中包含特殊字符",
     "密码中不包含特殊字符"
    ),
    (check_no_simple_sequence,
     "没发现简单连续序列",
     "警告：密码中包含简单连续序列，容易被猜测。"
    )
]

for function, success_message, failure_message in checks:
    result = function(password)
    display_result(result, success_message, failure_message)

print()
score = calculate_score(password)
print(f'密码得分:{score}/5')
print(f'密码强度:{get_strength(password)}')
print(get_password_feedback(password))
