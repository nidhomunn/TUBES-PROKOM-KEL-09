#ini bikinya disini ya ges
#SEMANGATTT!!

import csv

def load_user_data():
    # Load user data from the CSV file
    with open('datauser.csv', 'r') as file:
        reader = csv.reader(file)
        user_data = list(reader)
    return user_data

def save_user_data(user_data):
    # Save updated user data to the CSV file
    with open('datauser.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

def login():
    email = input ("enter your email:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username and user == email [1] and user[2] == password:
            return True

    return False

def signup():
    email = input ("enter your email:")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username:
            print("Username already exists. Please try again.")
            return

    user_data.append([username, password])
    save_user_data(user_data)
    print("Account created successfully. Please sign in.")

# Menu
print("Welcome!")
print("1. Sign In")
print("2. Sign Up")

choice = input("Choose an option: ")

if choice == "1":
    if login():
        print("Login successful!")
        # Call other functions or display menu after successful login
    else:
        print("Invalid username or password.")
        # Call login function again or display error message
elif choice == "2":
    signup()
else:
    print("Invalid option.")
