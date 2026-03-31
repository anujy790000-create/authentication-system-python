# Import json module for storing user data permanently
import json

# File where user data will be stored
FILE = "users.json"


# Load users from JSON file
def load_users():
    try:
        # Open file in read mode
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        # Return empty dictionary if file does not exist
        return {}


# Save users data into JSON file
def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


# Function to create new user account
def signup():
    users = load_users()

    username = input("Enter username: ")

    # Check if username already exists
    if username in users:
        print("User already exists!")
        return

    password = input("Enter password: ")

    # Store username and password
    users[username] = password
    save_users(users)

    print("Signup successful!")


# Function to login existing user
def login():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    # Verify credentials
    if users.get(username) == password:
        print("Login successful ✅")
    else:
        print("Invalid credentials ❌")


# Main program loop
while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    else:
        print("Exiting program...")
        break
