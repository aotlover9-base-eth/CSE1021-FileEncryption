# File Encryption/Decryption Tool

A simple, human-friendly command-line tool to encrypt and decrypt files using AES encryption.

## Features

- **Generate encryption keys** - Create secure encryption keys with flexible save locations
- **Encrypt files** - Secure your sensitive files with AES encryption, save anywhere you want
- **Decrypt files** - Restore encrypted files back to original, choose where to save
- **Batch operations** - Encrypt/decrypt multiple files at once
- **Key management** - Save and load encryption keys with custom locations
- **Flexible file storage** - Save encrypted/decrypted files in custom locations or ~/Downloads/keys
- **User-friendly interface** - Simple menu-based CLI with clear options

## Requirements

- Python 3.7 or higher
- `cryptography` library

## Installation & Setup

### 1. Clone or download the project
```bash
git clone https://github.com/aotlover9-base-eth/CSE1021-FileEncryption.git
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
3. Choose where to save it:
   - **Option 1:** Save manually - Enter custom path (e.g., `/home/user/keys/mykey.key`)
   - **Option 2:** Save in Downloads/keys - Automatically saves to `~/Downloads/keys/` folder (creates it if needed)

**Important:** Keep your key file safe! Without it, you cannot decrypt files.

### Step 2: Encrypt a File
1. Choose option **2** - "Encrypt a file"
2. Enter the file path you want to encrypt (e.g., `secret.txt`)
3. Enter your key file path
4. Choose where to save the encrypted file:
   - **Option 1:** Save manually - Enter custom path
   - **Option 2:** Save in Downloads/keys - Automatically saves to `~/Downloads/keys/` folder
5. The encrypted file will be saved to your chosen location

Example:
```
Original file: secret.txt
Encrypted file: ~/Downloads/keys/secret.txt.encrypted
```

### Step 3: Decrypt a File
1. Choose option **3** - "Decrypt a file"
2. Enter the encrypted file path
3. Enter your key file path
4. Choose where to save the decrypted file:
   - **Option 1:** Save manually - Enter custom path
   - **Option 2:** Save in Downloads/keys - Automatically saves to `~/Downloads/keys/` folder
5. The decrypted file will be saved to your chosen location

Example:
```
Encrypted file: ~/Downloads/keys/secret.txt.encrypted
Decrypted file: ~/Downloads/keys/secret.txt
```

### Multiple Files (Options 4 & 5)
- Choose **4** to encrypt multiple files at once
- Choose **5** to decrypt multiple files at once
- Enter the number of files and their paths
- Each file will ask you where to save the encrypted/decrypted version

## Save Location Features (NEW!)

### Option 1: Save Manually
Choose this if you want to save files in a specific location:
- You type the complete path with filename
- Example: `/home/user/my-documents/secret.txt`
- Works with absolute paths (recommended) or relative paths

### Option 2: Save in Downloads/keys
Choose this for organized, automatic storage:
- Files save to `~/Downloads/keys/` folder
- The folder is created automatically if it doesn't exist
- Just enter a filename, the tool handles the rest
- Example: Type `mykey.key` → Saves to `~/Downloads/keys/mykey.key`

**Benefits:**
- ✅ All keys and files in one organized place
- ✅ No need to remember paths
- ✅ Automatic folder creation
- ✅ Clean and organized file management

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
- `get_save_location()` - Asks user where to save a file (custom path or Downloads/keys folder)
- `save_key()` - Saves key to file with automatic directory creation
- `load_key()` - Loads key from file
- `encrypt_file()` - Encrypts a single file and asks where to save
- `decrypt_file()` - Decrypts a single file and asks where to save
- `encrypt_multiple_files()` - Batch encryption with save location choice
- `decrypt_multiple_files()` - Batch decryption with save location choice

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
