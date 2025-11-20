import hashlib
import os

FILE_NAME = "credentials.txt"
DELIMITER = ";"

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def get_next_user_id() -> int:
    if not os.path.exists(FILE_NAME):
        return 0
    try:
        with open(FILE_NAME, 'r') as f:
            return sum(1 for line in f)
    except Exception:
        return 0

def register_user(username: str, hashed_password: str):
    user_id = get_next_user_id()
    data_line = f"{user_id}{DELIMITER}{username}{DELIMITER}{hashed_password}\n"
    with open(FILE_NAME, 'a') as f:
        f.write(data_line)

def authenticate_user(username: str, hashed_password: str) -> tuple[bool, tuple[str, str] | None]:
    if not os.path.exists(FILE_NAME):
        return False, None
        
    with open(FILE_NAME, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split(DELIMITER)
            
            if len(parts) == 3:
                stored_id = parts[0]
                stored_username = parts[1]
                stored_hash = parts[2]
                
                if stored_username == username and stored_hash == hashed_password:
                    return True, (stored_id, stored_username)
                    
    return False, None