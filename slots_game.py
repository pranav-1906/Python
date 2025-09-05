import time
import random

def spin():
    symbols = ['🍒','🍋','🍇','⭐','7️⃣']

    return[random.choice(symbols) for i in range(3)]

def check_win(reel,bet):
    if reel[0] == reel[1] == reel[2]:
        return bet*5
    elif reel[0] == reel[1] or reel[1] == reel[2] or reel[2] == reel[0]:
        return bet*2
    else:
        return 0

def main():
    balance = 100

    print("--------------------------------")
    print("-----Slots-----")
    print("Symbols : 🍒 🍋 🍇 ⭐  7️⃣")
    print("--------------------------------")

    while balance>0:

        print(f"Current balance: ${balance}")

        bet = input("Enter your bet(q to quit):")

        if bet.lower() == 'q':
            break      

        if not bet.isdigit():
            print("Enter a valid number!")
            print("--------------------------------")
            continue    
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient balance!")
            print("--------------------------------")
            continue

        if bet < 0:
            print("You can't enter negative numbers!")
            print("--------------------------------")
            continue

        balance -= bet

        print("Spinning...")
        time.sleep(2)
        print("----------------")
        reel = spin()
        print("   | ".join(reel))

        amount = check_win(reel,bet)

        balance += amount

        if amount > 0:
            print("----------------")
            print(f"You won ${amount} this round")
        else:
            print("----------------")
            print("You lost this round!")
    if balance == 0:
        print("--------------------------------")
        print("Sorry you have no money to bet!\nBetter luck next time!")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("See you later!")
        print("--------------------------------")


if __name__ == "__main__":
    main()