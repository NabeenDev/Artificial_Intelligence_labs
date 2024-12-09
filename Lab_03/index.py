# this program will check two number
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print(num1, " :is greater than: ", num2)
else:
    print(num2, " :is greater than: ", num1)

# this program check the weather
weather = input("Enter the weather (rainy, sunny, snowy): ").lower()
if weather == "sunny":
    print("It's a beautiful day! Go outside and enjoy!")
elif weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "snowy":
    print("Time for a snowball fight!")
else:
    print("I don't have advice for that kind of weather.")

# lab no 4
# this program will check username and password if your condition is correct so print the login successful and else your user name and password incorrect

user = input("Enter the User Number: ").lower()
password = int(input("Enter Your Password Must be in Number: "))

if user == "admin" and password == 12345:
    print("login successful")
else:
    print("your user name and password incorrect")


# lab no 4
# I have created A Simple ATM Machine. in which you can check your balance and perform withdraw amount task

balance = 50000
user_pin = int(input("Enter your ATM Pin: "))
if user_pin == 1234:
    print("do You want to check your detail.....")
    ask_question_from_user = str(input("write (YES or NO): ")).lower()
    if ask_question_from_user == "yes":
        print(
            " (1): if you want to check your Balance. \n (2): you want to perform some transaction."
        )
        user_perform_task = int(input("Enter Perform Options: "))
        if user_perform_task == 1:
            print("This is your Current Balance: ", balance)
            print("Thanks for Check Your Balance.....")
        elif user_perform_task == 2:
            print("Welcome to transaction")
            user_transaction_amount = int(input("Enter Your Withdraw Amount: "))
            balance -= user_transaction_amount
            print("Your Transaction has Been Successfully Complete.....")
            print("This is Your Remaining Amount: ", balance)
        else:
            print("Please Incorrect user input ")
    else:
        print("Thanks")
else:
    print("Incorrect PIN Please Try Again........")