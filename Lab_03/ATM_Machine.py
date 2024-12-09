
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
            print("you entered a wrong input. Please Try Again ")
    else:
        print("Thanks")
else:
    print("Incorrect PIN Please Try Again........")
