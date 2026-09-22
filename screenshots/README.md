# Screenshots & Demo Outputs

This folder contains demonstration outputs showing the new features of the File Encryption/Decryption Tool.

## Files in This Folder

### DEMO_OUTPUTS.txt
Complete demonstration of all new features with sample terminal outputs:

- **Screenshot 1**: Main application menu
- **Screenshot 2**: Generate key with 2 save location options (NEW!)
- **Screenshot 3**: Encrypt file with 2 save location options (NEW!)
- **Screenshot 4**: Decrypt file with 2 save location options (NEW!)
- **Screenshot 5**: Using custom save location (Option 1)
- **Screenshot 6**: File organization in ~/Downloads/keys folder

## Features Demonstrated

### 1. Encryption Key Save Location
When generating a new key, users can choose:
- **Option 1**: Save manually - specify custom path
- **Option 2**: Save in Downloads/keys - auto-creates ~/Downloads/keys folder

### 2. Encrypted File Save Location
When encrypting a file, users can choose:
- **Option 1**: Save manually - specify custom path
- **Option 2**: Save in Downloads/keys - keeps encrypted files organized

### 3. Decrypted File Save Location
When decrypting a file, users can choose:
- **Option 1**: Save manually - specify custom path
- **Option 2**: Save in Downloads/keys - keeps decrypted files organized

## How to Use These Outputs

1. Open `DEMO_OUTPUTS.txt` to see sample terminal interactions
2. Shows exactly how users interact with the new features
3. Demonstrates both save options (manual and automatic)
4. Shows the success messages and file organization

## Key Improvements

✅ Users no longer limited to single save location
✅ Automatic directory creation (no missing folder errors)
✅ Better file organization with Downloads/keys folder option
✅ Clear, user-friendly prompts
✅ Professional error handling

## Running the Tool Yourself

To see these outputs in action:

```bash
python3 main.py
```

Then follow the prompts:
1. Choose option 1, 2, or 3
2. When asked "Where would you like to save...", choose option 1 or 2
3. Follow the success messages to see where files are saved

---

**Note**: These are simulated outputs based on the actual tool functionality. The exact paths and timestamps may vary based on your system.
