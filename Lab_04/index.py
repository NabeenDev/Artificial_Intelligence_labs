# Task 1

# Program 1: Check if a number is even or odd
user_number = int(input("Enter any number: "))
if user_number % 2 == 0:
    print("This is an Even number.")
else:
    print("This is an Odd number.")

# Task 2: ATM Simulation

stored_pin = 4321  
current_balance = 2000  

# Step 1: Ask for PIN
entered_pin = int(input("Please input your PIN: "))  

# Step 2: Verify PIN
if entered_pin == stored_pin:
    print("\nPIN verified successfully. Access granted.")
    
    # Step 3: Display Options
    while True:
        print("\nOptions:")
        print("1. View Balance")
        print("2. Withdraw Funds")
        print("3. Log Out")
        
        # Step 4: Get User Selection
        selection = int(input("Select an option (1-3): "))  
        
        if selection == 1:
            # Option 1: Display balance
            print(f"Your available balance is: ${current_balance}")
            
        elif selection == 2:
            # Option 2: Withdraw funds
            amount_to_withdraw = int(input("Enter withdrawal amount: "))  

            if amount_to_withdraw <= current_balance:
                current_balance -= amount_to_withdraw
                print(f"You have withdrawn ${amount_to_withdraw}. Remaining balance: ${current_balance}")
            else:
                print("Insufficient balance to complete the transaction.")
                
        elif selection == 3:
            # Option 3: Exit
            print("Thank you for banking with us. Goodbye!")
            break
            
        else:
            print("Invalid input. Please choose a valid option.")
else:
    print("Invalid PIN. Access denied.")

# Task 3: Login System

stored_username = "user123"
stored_password = 67890

# Prompt for credentials
input_username = input("Enter your username: ")
input_password = int(input("Enter your password: "))

# Validate credentials
if input_username == stored_username and input_password == stored_password:
    print("Welcome! You have successfully logged in.")
elif input_username != stored_username:
    print("Username not recognized.")
elif input_password != stored_password:
    print("Incorrect password.")
