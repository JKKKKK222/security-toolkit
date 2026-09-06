import hashlib

def calculate_file_hash(file_path):
    try:
        with open(file_path,"rb") as file:
            data = file.read()
            return hashlib.sha256(data).hexdigest()
    except FileNotFoundError:
        return None

def verify_file_hash(file_path, expected_hash):
    actual_hash = calculate_file_hash(file_path)
    if actual_hash is None:
        return None
    elif actual_hash == expected_hash:
        return True
    return False
    