### Name : Aye Thida
### Student Id: M24W7510

import random

### Function to generate Withdraw Transaction ID
def gen_Wtrn():
    trn_no = int(random.random() * 100)
    withdraw_trn = "W" + str(trn_no)
    return withdraw_trn

### Function to generate Deposit Transaction ID
def gen_Dtrn():
    trn_no = int(random.random() * 100)
    deposit_trn = "D" + str(trn_no)
    return deposit_trn

### Dictionary to hold transactions
transactions = {}

### Menu options
deposit_menu = 'd'
withdraw_menu = 'w'
inquiry_menu = 't'
history_menu = 'h'
end_prom = 'q'

### Initial balances
balance_amt = 0

print("Choose the ATM Operation:")
print("Enter 'd' for deposit")
print("Enter 'w' for withdraw")
print("Enter 'h' for history")
print("Enter 't' for balance total inquiry")
print("Enter 'q' to quit")
print("===================================== \n")

while True:
    ### The input text has been converted to lowercase
    input_value = input("Enter operation value: ").lower()

    if input_value == deposit_menu:
        deposit_amt = int(input("Enter deposit amount: "))
        balance_amt += deposit_amt
        transactions[gen_Dtrn()] = deposit_amt
        print("Your deposited amount is:", deposit_amt)
        print("Current balance is:", balance_amt)

    elif input_value == withdraw_menu:
        withdraw_amt = int(input("Enter withdraw amount: "))
        if withdraw_amt <= balance_amt:
            balance_amt -= withdraw_amt

            ### Use a negative value for withdrawal
            transactions[gen_Wtrn()] = -withdraw_amt  
            print("Your withdrawn amount is:", withdraw_amt)
            print("Current balance is:", balance_amt)
        else:
            ###insuffiecient blance check
            print("Insufficient balance! Your current balance is:", balance_amt) 

    elif input_value == inquiry_menu:
        print("Your current total balance is:", balance_amt)
        

    elif input_value == history_menu:
        print("Transaction History:")
        for trn_id, amount in transactions.items():
            print(f"{trn_id}: {amount}")     

    elif input_value == end_prom:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid operation. Please try again.")