

import hashlib

# Store users (username -> hashed password)
users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")

    if username in users:
        print("Username already exists!")
        return

    password = input("Enter password: ")
    users[username] = hash_password(password)
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("User not found!")
        return

    if users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Incorrect password!")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
