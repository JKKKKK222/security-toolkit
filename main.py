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
import getpass
from modules.file_hash import (
    calculate_file_hash,
    verify_file_hash
)
from modules.url_analyzer import analyze_url
from modules.port_scanner import (
    scan_ports,
    scan_common_ports
)

def main():
    while True:
        print("1. Password Analyzer")
        print("2. File Hash Calculator")
        print("3. File Hash Verify")
        print("4. URL Analyzer")
        print("5. Port Scanner")
        print("6. Exit")
        choice = input("请选择功能：")
        if choice == "1":
            run_password_analyzer()
        
        elif choice == "2":
            run_file_hash_calculator()

        elif choice == "3":
            run_file_hash_verifier()

        elif choice == "4":
            run_url_analyzer()

        elif choice == "5":
            run_port_scanner()

        elif choice == "6":
            print("程序退出")
            break
        
        else:
            print("无效输入，请重新输入")

def run_password_analyzer():
    password = getpass.getpass("请输入一个密码：")
    for function, success_message, failure_message in checks:
        result = function(password)
        display_result(result, success_message, failure_message)
                
    print()
                
    score = calculate_score(password)
                
    print(f'密码得分:{score}/5')
    print(f'密码强度:{get_strength(password)}')
    print(get_password_feedback(password))

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

def run_file_hash_calculator():
    file_path = input("请输入文件路径:")
    algorithm = get_hash_algorithm()
    try:
        file_hash = calculate_file_hash(file_path, algorithm)
    except ValueError:
        print("不支持的哈希算法")
        return
    if file_hash is None:
        print("文件不存在")
    else:
        print(file_hash)

def run_file_hash_verifier():
    file_path = input("请输入文件路径:")
    algorithm = get_hash_algorithm()
    expected_hash = input("请输入期望的哈希值:")
    try:
        result = verify_file_hash(file_path, expected_hash, algorithm)
    except ValueError:
        print("不支持的哈希算法")
        return
    if result is None:
        print("文件不存在")
    elif result:
        print("文件哈希匹配")
    else:
        print("文件哈希不匹配")

def get_hash_algorithm():
    return input("请输入哈希算法(sha256/md5/sha1/sha512):").strip().lower()

def run_url_analyzer():
    url = input("请输入URL:")
    result = analyze_url(url)

    if result is None:
        print("URL 无效")
        return 

    print(f'URL:{url}')
    print(f'协议:{result["scheme"]}')
    print(f'主机名:{result["hostname"]}')
    print(f'是否使用 HTTPS:{"是" if result["uses_https"] else "否"}')
    print(f'是否使用 IP 地址:{"是" if result["uses_ip_address"]else "否"}')
    print(f'是否发现可疑端口:{"是" if result["suspicious_port"]else "否"}')
    print(f'是否过长:{"是" if result["too_long"]else "否"}')
    print(f'是否有@字符:{"是" if result["has_at_symbol"]else "否"}')
    print(f'风险分数:{result["risk_score"]}')
    print(f'风险级别:{result["risk_level"]}')

def run_port_scanner():
    print("1. Scan The Specified Port")
    print("2. Scan Common Port")
    print("3. Exit")
    while True:
        choice = input("请选择功能:")
        if choice == "1":
            host = input("请输入目标主机:").strip()
            try:
                start_port = int(input("请输入初始端口:"))
            except ValueError:
                print("端口形式输入错误")
                return

            try:
                end_port = int(input("请输入终止端口:"))
            except ValueError:
                print("端口形式输入错误")
                return
        
            result = scan_ports(host, start_port, end_port)
            if result is None:
                print("主机或端口范围无效")
                return
            break

        elif choice == "2":
            host = input("请输入目标主机:").strip()

            result = scan_common_ports(host)
            if result is None:
                print("目标主机无效")
                return
            break

        elif choice == "3":
            return

        else:
            print("输入无效，请重新输入")

if __name__ == "__main__":
    main()