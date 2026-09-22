#!/usr/bin/env python3

import os
import sys
from encryption import (
    generate_key, save_key, load_key,
    encrypt_file, decrypt_file,
    encrypt_multiple_files, decrypt_multiple_files
)

def print_banner():
    """Display welcome banner"""
    print("\n" + "="*50)
    print("  FILE ENCRYPTION/DECRYPTION TOOL")
    print("="*50 + "\n")

def print_menu():
    """Display main menu"""
    print("\nWhat do you want to do?\n")
    print("1. Generate a new encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Encrypt multiple files")
    print("5. Decrypt multiple files")
    print("6. Exit")
    print()

def get_user_choice():
    """Get user's menu choice"""
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("✗ Invalid choice. Please enter 1-6.")

def handle_generate_key():
    """Handle key generation"""
    print("\n--- Generate New Key ---")
    key = generate_key()
    print(f"New key generated: {key.decode()[:20]}...")

    save_location = input("\nEnter filename to save key (default: encryption.key): ").strip()
    if not save_location:
        save_location = "encryption.key"

    save_key(key, save_location)

def handle_encrypt_file():
    """Handle single file encryption"""
    print("\n--- Encrypt a File ---")

    file_to_encrypt = input("Enter file path to encrypt: ").strip()
    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if not key_file:
        key_file = "encryption.key"

    key = load_key(key_file)
    if key:
        encrypt_file(file_to_encrypt, key)

def handle_decrypt_file():
    """Handle single file decryption"""
    print("\n--- Decrypt a File ---")

    file_to_decrypt = input("Enter encrypted file path: ").strip()
    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if not key_file:
        key_file = "encryption.key"

    key = load_key(key_file)
    if key:
        decrypt_file(file_to_decrypt, key)

def handle_encrypt_multiple():
    """Handle multiple file encryption"""
    print("\n--- Encrypt Multiple Files ---")

    num_files = input("How many files to encrypt? ").strip()
    try:
        num_files = int(num_files)
    except ValueError:
        print("✗ Invalid number")
        return

    file_list = []
    for i in range(num_files):
        file_path = input(f"Enter file {i+1} path: ").strip()
        if file_path:
            file_list.append(file_path)

    if not file_list:
        print("✗ No files provided")
        return

    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if not key_file:
        key_file = "encryption.key"

    key = load_key(key_file)
    if key:
        encrypt_multiple_files(file_list, key)

def handle_decrypt_multiple():
    """Handle multiple file decryption"""
    print("\n--- Decrypt Multiple Files ---")

    num_files = input("How many files to decrypt? ").strip()
    try:
        num_files = int(num_files)
    except ValueError:
        print("✗ Invalid number")
        return

    file_list = []
    for i in range(num_files):
        file_path = input(f"Enter file {i+1} path: ").strip()
        if file_path:
            file_list.append(file_path)

    if not file_list:
        print("✗ No files provided")
        return

    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if not key_file:
        key_file = "encryption.key"

    key = load_key(key_file)
    if key:
        decrypt_multiple_files(file_list, key)

def main():
    """Main application loop"""
    print_banner()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == '1':
            handle_generate_key()
        elif choice == '2':
            handle_encrypt_file()
        elif choice == '3':
            handle_decrypt_file()
        elif choice == '4':
            handle_encrypt_multiple()
        elif choice == '5':
            handle_decrypt_multiple()
        elif choice == '6':
            print("\nGoodbye! Your files are safe.\n")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.\n")
        sys.exit(0)
