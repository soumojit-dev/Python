bank_accounts = {}

def create_account():
    username = input("Enter Username: ")
    if username in bank_accounts:
        print("Account already exists!")
    else:
        bank_accounts[username] = 0
        print(f"Account created for {username}")

def deposit():
    username = input("Enter Username: ")
    if username in bank_accounts:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            bank_accounts[username]+= amount
            print(f"{amount} is successfully deposited in {username}'s account!")
        else:
            print("Invalid Amount!")
    else:
        print("Account not found!")

def withdraw():
    username = input("Enter Username: ")
    if username in bank_accounts:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount < bank_accounts[username]:
            bank_accounts[username]-= amount
            print(f"{amount} withdrawal is successful from {username}'s account!")
        else:
            print(f"Insufficient Balance in {username}'s account!")
    else:
        print("Account not found!")

def balance():
    username = input("Enter Username: ")
    if username in bank_accounts:
        print(f"{username}'s account balance : {bank_accounts[username]}")
    else:
        print("Account not found!")

def display():
    while True:
        print("\n----Banking Operations----\n")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Account Balance")
        print("5. Exit")

        ch = int(input("Enter your choice (1-5): "))
        if ch == 1:
            create_account()
        elif ch == 2:
            deposit()
        elif ch == 3:
            withdraw()
        elif ch == 4:
            balance()
        elif ch == 5:
            print("Exiting....Thank you for banking with us!!")
        else:
            print("Enter Valid Choice (1-5)")
display()

# TEST CASE
# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 1
# Enter Username: Soumojit
# Account created for Soumojit

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 2
# Enter Username: Soumojit
# Enter amount to deposit: 35000
# 35000.0 is successfully deposited in Soumojit's account!

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 3
# Enter Username: Soumojit
# Enter withdrawal amount: 5000 
# 5000.0 withdrawal is successful from Soumojit's account!

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 4
# Enter Username: Soumojit
# Soumojit's account balance : 30000.0

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 5
# Exiting....Thank you for banking with us!!

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit
# Enter your choice (1-5): 2
# Enter Username: rony
# Account not found!

# ----Banking Operations----

# 1. Create New Account
# 2. Deposit
# 3. Withdraw
# 4. Check Account Balance
# 5. Exit

