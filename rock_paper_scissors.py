import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

rules = {
    ("rock", "scissors"): "Rock smashes scissors!",
    ("scissors", "paper"): "Scissors cuts paper!",
    ("paper", "rock"): "Paper covers rock!"
}

for round_num in range(1, 4):
    print(f"\nRound {round_num}:")
    
    player = input("Enter a choice (rock, paper, scissors): ").lower()
    while player not in choices:
        player = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    
    computer = random.choice(choices)
    print(f"Computer chose {computer}.")
    
    if player == computer:
        print(f"Both chose {player}. It's a tie!")
    elif (player, computer) in rules:
        print(rules[(player, computer)], "Player wins!")
        player_score += 1
    elif (computer, player) in rules:
        print(rules[(computer, player)], "Computer wins!")
        computer_score += 1

print("\n--- Final Score ---")
print(f"Player: {player_score} | Computer: {computer_score}")
if player_score > computer_score:
    print("Player wins the game!")
elif player_score < computer_score:
    print("Computer wins the game!")
else:
    print("It's a tie!")
