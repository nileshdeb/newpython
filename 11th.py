balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter the amount you want to withdraw: "))

if withdraw > balance:
    print("Insufficient funds.")
else:
    new_balance = balance - withdraw
    print(f"You have withdrawn ${withdraw}. Your new balance is ${new_balance}.")

