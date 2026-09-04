from modules.password_analyzer import check_password_length
password = input("请输入一个密码：")
result = check_password_length(password)
if result:
    print("密码长度符合基本要求。")
else:
    print("密码长度过短，建议至少使用 8 个字符。")