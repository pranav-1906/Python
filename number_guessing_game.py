import random

number = random.randint(1,20)
ans = False
for i in range(1,6):
    guess = int(input(f"Guess {i}:"))
    if guess == number:
        print(f"Congratulations, you guessed the number {number} in {i} attempts!")
        ans = True
        break
    elif guess < number:
        print(f"The number is greater than {guess}.")
    elif guess > number:
        print (f"The number is lower then {guess}.")
    else:
        print(f"Invalid input, please enter a valid number.")

if ans == False:
    print(f"Sorry! You're out of attempts. The number was {number}.")