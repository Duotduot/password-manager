import json
from cryptography.fernet import Fernet

PASSWORD_FILE = 'passwords.json'

# User Interface. Inputs 
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
main()