# security-toolkit
Description: A lightweight Python security toolkit for cybersecurity learning and practice

## Features
- Password length validation
- Common weak password detection
- Simple sequence detection
- Password strength evaluation
- Hidden password input
- SHA-256 file hash calculation
- SHA-256 file integrity verification

## Usage
Run the program with:
```bash
python main.py
```
Choose a function from the interactive menu. Password input is hidden for security.

Choose a function from the interactive menu:
1. Password Analyzer
2. File Hash Calculator
3. File Hash Verify
4. Exit

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

## Project Structure
```text
security-toolkit/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── password_analyzer.py
│   └── file_hash.py
├── README.md
├── .gitignore
└── LICENSE
```

- `main.py`: Program entry point and interactive menu.
- `modules/password_analyzer.py`: Password analysis and security check logic.
- `modules/file_hash.py`: SHA-256 file hash calculation and verification logic.

## License

This project is licensed under the MIT license.

## Requirement

` python 3.13+

## Future Improvements

- Add more password security rules
- Add configurable weak password dictionaries
- Add unit tests
- Add a command-line interface