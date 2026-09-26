from cryptography.fernet import Fernet, InvalidToken
import os
from pathlib import Path

def generate_key():
    """Generate a new encryption key"""
    key = Fernet.generate_key()
    return key

def get_save_location(file_type="file"):
    """
    Ask user where to save a file
    Returns the full path where file should be saved
    """
    print(f"\nWhere would you like to save the {file_type}?\n")
    print("1. Save manually (choose custom location)")
    print("2. Save in Downloads/keys folder")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == '1':
        filename = input(f"Enter filename for {file_type}: ").strip()
        if not filename:
            filename = "encryption.key" if file_type == "encryption key" else file_type

        # In case user entered a path in the filename, extract the base filename
        file_dir_from_name = os.path.dirname(filename)
        if file_dir_from_name:
            filename = os.path.basename(filename)

        file_path = input("Enter file path: ").strip()
        if not file_path:
            file_path = file_dir_from_name if file_dir_from_name else "."
        file_path = os.path.expanduser(file_path)

        # If user entered the full filepath including filename in file_path, avoid duplicate
        clean_path = file_path.rstrip("/\\")
        if os.path.basename(clean_path) == filename:
            save_path = file_path
        else:
            save_path = os.path.join(file_path, filename)

        if os.path.isdir(save_path):
            print(f"✗ Error: '{save_path}' is a directory, not a file.")
            return None

        return save_path

    elif choice == '2':
        # Get Downloads folder path
        downloads_path = str(Path.home() / "Downloads")
        keys_folder = os.path.join(downloads_path, "keys")

        # Create keys folder if it doesn't exist
        if not os.path.exists(keys_folder):
            os.makedirs(keys_folder)
            print(f"✓ Created folder: {keys_folder}")

        filename = input(f"Enter filename for {file_type} (default: {file_type}): ").strip()
        if not filename:
            filename = file_type

        save_path = os.path.join(keys_folder, filename)
        if os.path.isdir(save_path):
            print(f"✗ Error: '{save_path}' is a directory, not a file.")
            return None
        return save_path

    else:
        print("✗ Invalid choice")
        return None

def save_key(key, key_filename):
    """Save the encryption key to a file"""
    if os.path.isdir(key_filename):
        print(f"✗ Error: '{key_filename}' is a directory, not a file.")
        return False

    try:
        # Create directory if it doesn't exist
        key_directory = os.path.dirname(key_filename)
        if key_directory and not os.path.exists(key_directory):
            os.makedirs(key_directory)

        with open(key_filename, 'wb') as key_file:
            key_file.write(key)
        print(f"✓ Key saved to: {key_filename}")
        return True
    except IsADirectoryError:
        print(f"✗ Error: '{key_filename}' is a directory, not a file.")
        return False
    except Exception as e:
        print(f"✗ Failed to save key: {e}")
        return False

def load_key(key_filename):
    """Load the encryption key from a file"""
    if not os.path.exists(key_filename):
        print(f"✗ Key file not found: {key_filename}")
        return None

    if os.path.isdir(key_filename):
        print(f"✗ Error: '{key_filename}' is a directory, not a file.")
        return None

    try:
        with open(key_filename, 'rb') as key_file:
            key = key_file.read()
        return key
    except IsADirectoryError:
        print(f"✗ Error: '{key_filename}' is a directory, not a file.")
        return None
    except Exception as e:
        print(f"✗ Failed to load key: {e}")
        return None

def encrypt_file(file_path, key):
    """Encrypt a file and ask where to save it"""
    if not os.path.exists(file_path):
        print(f"✗ File not found: {file_path}")
        return False

    if os.path.isdir(file_path):
        print(f"✗ Error: '{file_path}' is a directory, not a file.")
        return False

    try:
        cipher = Fernet(key)

        with open(file_path, 'rb') as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)

        # Ask user where to save encrypted file
        encrypted_filename = get_save_location("encrypted file")

        if encrypted_filename is None:
            return False

        if os.path.isdir(encrypted_filename):
            print(f"✗ Error: '{encrypted_filename}' is a directory, not a file.")
            return False

        # Create directory if it doesn't exist
        encrypted_directory = os.path.dirname(encrypted_filename)
        if encrypted_directory and not os.path.exists(encrypted_directory):
            os.makedirs(encrypted_directory)

        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        file_size_kb = os.path.getsize(file_path) / 1024
        print(f"\n✓ File encrypted successfully!")
        print(f"  Original: {file_path}")
        print(f"  Encrypted: {encrypted_filename}")
        print(f"  Size: {file_size_kb:.2f} KB")
        return True

    except IsADirectoryError:
        print("✗ Error: Cannot encrypt a directory.")
        return False
    except Exception as e:
        print(f"✗ Encryption failed: {e}")
        return False

def decrypt_file(encrypted_file_path, key):
    """Decrypt a file and ask where to save it"""
    if not os.path.exists(encrypted_file_path):
        print(f"✗ File not found: {encrypted_file_path}")
        return False

    if os.path.isdir(encrypted_file_path):
        print(f"✗ Error: '{encrypted_file_path}' is a directory, not a file.")
        return False

    try:
        cipher = Fernet(key)

        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        # Ask user where to save decrypted file
        decrypted_filename = get_save_location("decrypted file")

        if decrypted_filename is None:
            return False

        if os.path.isdir(decrypted_filename):
            print(f"✗ Error: '{decrypted_filename}' is a directory, not a file.")
            return False

        # Create directory if it doesn't exist
        decrypted_directory = os.path.dirname(decrypted_filename)
        if decrypted_directory and not os.path.exists(decrypted_directory):
            os.makedirs(decrypted_directory)

        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        file_size_kb = os.path.getsize(decrypted_filename) / 1024
        print(f"\n✓ File decrypted successfully!")
        print(f"  Encrypted: {encrypted_file_path}")
        print(f"  Decrypted: {decrypted_filename}")
        print(f"  Size: {file_size_kb:.2f} KB")
        return True

    except InvalidToken:
        print("✗ Wrong key! Cannot decrypt file.")
        return False
    except IsADirectoryError:
        print("✗ Error: Cannot decrypt a directory.")
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
