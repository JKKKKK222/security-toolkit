import hashlib

def calculate_file_hash(file_path,algorithm="sha256"):
    try:
        with open(file_path,"rb") as file:
            data = file.read()
            if algorithm == "sha256":
                return hashlib.sha256(data).hexdigest()
            elif algorithm == "md5":
                return hashlib.md5(data).hexdigest()
            elif algorithm == "sha1":
                return hashlib.sha1(data).hexdigest()
            elif algorithm == "sha512":
                return hashlib.sha512(data).hexdigest()
            else:
                raise ValueError("不支持的哈希算法")
    except FileNotFoundError:
        return None

def verify_file_hash(file_path, expected_hash, algorithm="sha256"):
    expected_hash = expected_hash.strip().lower()
    actual_hash = calculate_file_hash(file_path, algorithm)
    if actual_hash is None:
        return None
    elif actual_hash == expected_hash:
        return True
    return False
    