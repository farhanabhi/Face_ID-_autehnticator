from cryptography.fernet import Fernet

def save_key(path):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)

def load_key(path):
    with open(path, "rb") as f:
        return f.read()

def encrypt_data(path, data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(path, "wb") as f:
        f.write(encrypted)

def decrypt_data(path, key):
    fernet = Fernet(key)
    with open(path, "rb") as f:
        encrypted = f.read()
    return fernet.decrypt(encrypted)