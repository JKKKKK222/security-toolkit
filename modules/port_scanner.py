import socket
import time

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate",
    27017: "MongoDB"
}

def check_port(host, port, check_time = 0.5):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(check_time)
    try:
        return sock.connect_ex((host, port)) == 0
    except socket.error:
        return False
    finally:
        sock.close()
    

def scan_ports(host, start_port, end_port):
    try:
        resolved_host = socket.gethostbyname(host)
    except socket.gaierror:
        print("该域名无法解析")
        return None
    open_ports = []
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("端口范围无效")
        return None

    total_ports = end_port - start_port + 1

    print(f'目标主机: {host}')
    print(f'目标IP: {resolved_host}')
    print(f'扫描范围: {start_port} - {end_port}')

    print("正在扫描...")
    start_time = time.time()
    for index, port in enumerate(range(start_port, end_port + 1), start=1):
        print(f'扫描进度: {index/total_ports*100:.2f}%',end = '\r')
        if check_port(resolved_host, port):
            open_ports.append(port)
            print()
            print(f'{port} OPEN {COMMON_PORTS.get(port, "Unknown")}')
    end_time = time.time()

    print()

    elapsed_time = end_time - start_time
    print("--------------------------")
    print("扫描完成")
    print(f'扫描耗时: {elapsed_time:.2f} 秒')
    if not open_ports:
        print("未发现开放端口")
    else:
        print(f'共发现 {len(open_ports)} 个开放端口')
    return open_ports

def scan_common_ports(host):
    try:
        resolved_host = socket.gethostbyname(host)
    except socket.gaierror:
        print("该域名无法解析")
        return None

    open_ports = []

    print(f'目标主机: {host}')
    print(f'目标IP: {resolved_host}')
    print("正在扫描常见端口...")

    total_ports = len(COMMON_PORTS)
    start_time = time.time()
    for index, port in enumerate(COMMON_PORTS.keys(), start=1):
        print(f'扫描进度: {index/total_ports*100:.2f}%',end='\r')
        if check_port(resolved_host, port, 0.2):
            open_ports.append(port)
            print()
            print(f'{port} OPEN {COMMON_PORTS.get(port, "Unknown")}')
    end_time = time.time()
    elapsed_time = end_time - start_time

    print()

    print("----------------------")
    print("扫描完成")
    print(f'扫描耗时: {elapsed_time:.2f} 秒')
    
    if not open_ports:
        print("未发现开放端口")
    else:
        print(f'共发现 {len(open_ports)} 个开放端口')

    return open_ports