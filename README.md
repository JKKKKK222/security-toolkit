# security-toolkit
Description: A lightweight Python security toolkit for cybersecurity learning and practice

## Features
- Password length validation
- Common weak password detection
- Simple sequence detection
- Password strength evaluation
- Hidden password input

## Usage
Run the program with:
```bash
python main.py
```
Enter a password when prompted. The input will be hidden for security.

## Example
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

## Project Structure
```text
security-toolkit/
├── main.py
├── modules/
│   ├── __init__.py
│   └── password_analyzer.py
├── README.md
├── .gitignore
└── LICENSE
```

- `main.py`: Program entry point and user interaction.
- `modules/password_analyzer.py`: Password analysis and security check logic.

## License

This project is licensed under the MIT license.

## Requirement

` python 3.13+

## Future Improvements

- Add more password security rules
- Add configurable weak password dictionaries
- Add unit tests
- Add a command-line interface