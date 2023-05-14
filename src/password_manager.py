import json
import os
import getpass
import hashlib
from cryptography.fernet import Fernet

PASSWORD_FILE = 'passwords.json'

# User Interface which includes input.
def main():
    print("Welcome to the Password Manager")
    print("Please choose an option from the menu below:")
    while True:
        print("1. Show Passwords")
        print("2. Add Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_passwords()
        elif choice == '2':
            add_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("Thank you for using Password Manager")
            break
        else:
            print("Invalid choice. Please try again.")

# Defining Functions

# Show Password Function
def show_passwords():
    if not os.path.isfile(PASSWORD_FILE):
        print("No passwords saved yet.")
        return
    
    with open(PASSWORD_FILE, 'r') as f:
        passwords = json.load(f)

    print("Here are your saved passwords:")
    for site, password in passwords.items():
        print(f"{site}: {decrypt_password(password)}")

# Retrieve Password Function
def add_password():
    site = input("Enter the site name: ")
    password = getpass.getpass("Enter the password: ")

    with open(PASSWORD_FILE, 'a+') as f:
        f.seek(0)
        contents = f.read()
        if contents:
            passwords = json.loads(contents)
        else:
            passwords = {}
        
        passwords[site] = encrypt_password(password)

        f.seek(0)
        f.truncate()
        json.dump(passwords, f)
    
    print("Password saved successfully.")

# Delete Password Function
def delete_password():
    if not os.path.isfile(PASSWORD_FILE):
        print("No passwords saved yet.")
        return 
    
    site = input("Enter the site name: ")

    with open(PASSWORD_FILE, 'r') as f:
        passwords = json.load(f)

    if site in passwords:
        del passwords[site]
        with open(PASSWORD_FILE, 'w') as f:
            json.dump(passwords, f)
        print(f"{site}'s password deleted successfully.")
    else:
        print(f"No password found for {site}.")

#Encrypt passwords funtion 
def encrypt_password(password):
    salt = b'salt_for_password_manager'
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key.hex()

# Decrypt passwords function 
def decrypt_password(password_hash):
    return "********"

if __name__ == '__main__':
    main()