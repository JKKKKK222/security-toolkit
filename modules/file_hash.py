import hashlib

def calculate_file_hash(file_path):
    try:
        with open(file_path,"rb") as file:
            data = file.read()
            return hashlib.sha256(data).hexdigest()
    except FileNotFoundError:
        return None