correct_username = "Nabeen"
correct_password = 5777

# Prompt user for input
username = input("Enter username: ")
password = int(input("Enter password: "))

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Incorrect username")
else:
    print("Incorrect password")