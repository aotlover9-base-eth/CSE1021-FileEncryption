from cryptography.fernet import Fernet, InvalidToken
import os

def generate_key():
    """Generate a new encryption key and save it to a file"""
    key = Fernet.generate_key()
    return key

def save_key(key, key_filename):
    """Save the encryption key to a file"""
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)
    print(f"✓ Key saved to: {key_filename}")

def load_key(key_filename):
    """Load the encryption key from a file"""
    if not os.path.exists(key_filename):
        print(f"✗ Key file not found: {key_filename}")
        return None

    with open(key_filename, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_path, key):
    """Encrypt a file and save as .encrypted"""
    if not os.path.exists(file_path):
        print(f"✗ File not found: {file_path}")
        return False

    try:
        cipher = Fernet(key)

        with open(file_path, 'rb') as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)

        encrypted_filename = file_path + '.encrypted'
        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        file_size_kb = os.path.getsize(file_path) / 1024
        print(f"✓ File encrypted successfully!")
        print(f"  Original: {file_path}")
        print(f"  Encrypted: {encrypted_filename}")
        print(f"  Size: {file_size_kb:.2f} KB")
        return True

    except Exception as e:
        print(f"✗ Encryption failed: {e}")
        return False

def decrypt_file(encrypted_file_path, key):
    """Decrypt a file and save as .decrypted"""
    if not os.path.exists(encrypted_file_path):
        print(f"✗ File not found: {encrypted_file_path}")
        return False

    try:
        cipher = Fernet(key)

        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        # Remove .encrypted extension and add .decrypted
        if encrypted_file_path.endswith('.encrypted'):
            decrypted_filename = encrypted_file_path[:-10] + '.decrypted'
        else:
            decrypted_filename = encrypted_file_path + '.decrypted'

        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        file_size_kb = os.path.getsize(decrypted_filename) / 1024
        print(f"✓ File decrypted successfully!")
        print(f"  Encrypted: {encrypted_file_path}")
        print(f"  Decrypted: {decrypted_filename}")
        print(f"  Size: {file_size_kb:.2f} KB")
        return True

    except InvalidToken:
        print("✗ Wrong key! Cannot decrypt file.")
        return False
    except Exception as e:
        print(f"✗ Decryption failed: {e}")
        return False

def encrypt_multiple_files(file_list, key):
    """Encrypt multiple files at once"""
    success_count = 0
    failed_count = 0

    print(f"\nEncrypting {len(file_list)} files...\n")

    for file_path in file_list:
        if encrypt_file(file_path, key):
            success_count += 1
        else:
            failed_count += 1
        print()

    print(f"Summary: {success_count} encrypted, {failed_count} failed")
    return success_count, failed_count

def decrypt_multiple_files(file_list, key):
    """Decrypt multiple files at once"""
    success_count = 0
    failed_count = 0

    print(f"\nDecrypting {len(file_list)} files...\n")

    for file_path in file_list:
        if decrypt_file(file_path, key):
            success_count += 1
        else:
            failed_count += 1
        print()

    print(f"Summary: {success_count} decrypted, {failed_count} failed")
    return success_count, failed_count
