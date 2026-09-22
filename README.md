# File Encryption/Decryption Tool

A simple, human-friendly command-line tool to encrypt and decrypt files using AES encryption.

## Features

- **Generate encryption keys** - Create secure encryption keys
- **Encrypt files** - Secure your sensitive files with AES encryption
- **Decrypt files** - Restore encrypted files back to original
- **Batch operations** - Encrypt/decrypt multiple files at once
- **Key management** - Save and load encryption keys
- **User-friendly interface** - Simple menu-based CLI

## Requirements

- Python 3.7 or higher
- `cryptography` library

## Installation & Setup

### 1. Clone or download the project
```bash
git clone https://github.com/YOUR-USERNAME/CSE1021-FileEncryption.git
cd CSE1021-FileEncryption
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install cryptography==42.0.5
```

### 3. Make the script executable (Linux/Mac)
```bash
chmod +x main.py
```

## How to Run

### Start the application:
```bash
python3 main.py
```

Or on Linux/Mac:
```bash
./main.py
```

## Usage Guide

### Step 1: Generate a Key
When you run the application for the first time:
1. Choose option **1** - "Generate a new encryption key"
2. A new key will be generated
3. Save it with a name like `encryption.key`

**Important:** Keep your key file safe! Without it, you cannot decrypt files.

### Step 2: Encrypt a File
1. Choose option **2** - "Encrypt a file"
2. Enter the file path you want to encrypt (e.g., `secret.txt`)
3. Enter your key file path (default: `encryption.key`)
4. The tool will create an encrypted copy with `.encrypted` extension

Example:
```
Original file: secret.txt
Encrypted file: secret.txt.encrypted
```

### Step 3: Decrypt a File
1. Choose option **3** - "Decrypt a file"
2. Enter the encrypted file path
3. Enter your key file path
4. The tool will create a decrypted copy with `.decrypted` extension

Example:
```
Encrypted file: secret.txt.encrypted
Decrypted file: secret.txt.decrypted
```

### Multiple Files (Options 4 & 5)
- Choose **4** to encrypt multiple files at once
- Choose **5** to decrypt multiple files at once
- Enter the number of files and their paths

## File Structure

```
CSE1021-FileEncryption/
├── main.py              # Main application entry point
├── encryption.py        # Encryption/decryption logic
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── Statement.md        # Problem statement
└── screenshots/        # Output screenshots
```

## Example Workflow

```bash
# 1. Start the app
python3 main.py

# 2. Generate key
# Choose: 1
# Save as: my_encryption.key

# 3. Create a test file
echo "This is a secret message" > secret.txt

# 4. Encrypt it
# Choose: 2
# File path: secret.txt
# Key file: my_encryption.key

# 5. Decrypt it
# Choose: 3
# Encrypted file: secret.txt.encrypted
# Key file: my_encryption.key
```

## Security Notes

- **Key Storage:** Keep your `.key` file in a safe location
- **Backup Keys:** Make copies of your encryption keys
- **Strong Keys:** The tool generates cryptographically strong keys automatically
- **Encryption Method:** Uses Fernet (AES-128 encryption)

## What Each File Does

### main.py
- Displays the user menu
- Handles user input
- Calls encryption functions based on user choice

### encryption.py
- `generate_key()` - Creates a new encryption key
- `save_key()` - Saves key to file
- `load_key()` - Loads key from file
- `encrypt_file()` - Encrypts a single file
- `decrypt_file()` - Decrypts a single file
- `encrypt_multiple_files()` - Batch encryption
- `decrypt_multiple_files()` - Batch decryption

## Troubleshooting

### Error: "Key file not found"
- Make sure your encryption key file exists in the specified path
- Check the file name and path are correct

### Error: "Wrong key! Cannot decrypt file"
- You're using the wrong encryption key
- Make sure you're using the same key that encrypted the file

### Error: "File not found"
- Check that the file path is correct
- Use absolute paths if relative paths don't work

### Module not found: cryptography
- Install dependencies: `pip install -r requirements.txt`

## License

This project is created for educational purposes.

## Author

Created as a Python Essentials course project.
