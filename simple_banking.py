def chkbalance():
    print(f"Your balance: {balance}")

def deposit():
    depo = int(input("Enter amount to deposit:"))
    if depo <= 0:
        print("Invalid amount!")
        return 0
    else:
        return depo

def withdraw():
    withd = int(input("Enter amount to withdraw:"))
    if withd > balance:
        print("Insufficient Balance!")
        return 0
    else:
        return withd

balance = 0

while True:
    print("-------Banking--------")
    print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice = int(input("Enter your choice(1-4):"))

    match choice:
        case 1:
            print('------------------------')
            chkbalance()
            print('------------------------')
        case 2:
            print('------------------------')
            balance += deposit()
            print('------------------------')
        case 3:
            print('------------------------')
            balance -= withdraw()
            print('------------------------')
        case 4:
            break
        case _:
            print('------------------------')
            print("That's not a valid input!")
            print('------------------------')

print("Thank you have a good day!")