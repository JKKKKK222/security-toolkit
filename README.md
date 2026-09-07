# security-toolkit
Description: A lightweight Python security toolkit for cybersecurity learning and practice

## Features

### Password Analyzer
- Password length validation
- Common weak password detection
- Simple sequence detection
- Password strength evaluation
- Hidden password input

### File Hash Tools
- File hash calculation with multiple algorithms
- Supports MD5,SHA-1,SHA-256,and SHA-512
- File hash verification for integrity checking

### URL Analyzer
- URL parsing and structure analysis
- HTTPS detection
- IP address detection
- Suspicious port detection
- @ symbol detection
- Long URL detection
- Risk scoring
- Risk level classification (Low, Medium, High)

## Usage
Run the program with:
```bash
python main.py
```
Choose a function from the interactive menu. Password input is hidden for security.

1. Password Analyzer
2. File Hash Calculator
3. File Hash Verify
4. URL Analyzer
5. Exit

## Example

### Password Analyzer
```text
请输入一个密码：

密码长度符合基本要求。
密码中包含数字字符
密码中包含大写字母
密码中包含小写字母
密码中包含特殊字符
没发现简单连续序列

密码得分:5/5
密码强度:Strong
未发现常见弱密码风险。
```

### File Hash Calculator
```text
请输入文件路径:text.txt
48a781cfd96c121b25ac63c902497741841b78166097d0316f72a62f46552e3a
```

### File Hash verify
```text
请输入文件路径:text.txt
请输入期望的 SHA-256 哈希值:48a781cfd96c121b25ac63c902497741841b78166097d0316f72a62f46552e3a
文件哈希匹配
```

### URL Analyzer
```text
请输入URL:http://127.0.0.1:8080/login
URL:http://127.0.0.1:8080/login
协议:http
主机名:127.0.0.1
是否使用 HTTPS:否
是否使用 IP 地址:是
是否发现可疑端口:是
是否过长:否
是否有@字符:否
风险分数:4
风险级别:High
```

## Project Structure
```text
security-toolkit/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── password_analyzer.py
│   ├── file_hash.py
│   └── url_analyzer.py
├── README.md
├── .gitignore
└── LICENSE
```

- `main.py`: Program entry point and interactive menu.
- `modules/password_analyzer.py`: Password analysis and security check logic.
- `modules/file_hash.py`: File hash calculation and verification logic.
- `modules/url_analyzer.py`: URL parsing, suspicious characteristic detection, and risk scoring logic.

## License

This project is licensed under the MIT license.

## Requirement

` python 3.13+

## Future Improvements

- Add more password security rules
- Add configurable weak password dictionaries
- Add more URL risk detection rules
- Add configurable URL risk scoring
- Add unit tests
- Add a command-line interface