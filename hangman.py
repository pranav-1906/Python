import random

words = [
    "apple", "banana", "orange", "mango", "grape", "cherry", "melon", "kiwi",
    "papaya", "lemon", "lime", "apricot", "fig", "guava", "pear", "peach",
    "plum", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry",
    "watermelon", "coconut", "pomegranate", "lychee",

    "tiger", "lion", "elephant", "zebra", "giraffe", "monkey", "panda",
    "kangaroo", "bear", "rabbit", "wolf", "fox", "deer", "camel", "goat",
    "sheep", "horse", "donkey", "buffalo", "dog", "cat", "leopard", "cheetah",
    "crocodile", "eagle", "owl", "snake", "turtle", "dolphin", "whale",

    "chair", "table", "pencil", "bottle", "laptop", "mobile", "keyboard",
    "mouse", "window", "door", "fan", "light", "book", "notebook", "pen",
    "glasses", "spoon", "plate", "cup", "clock", "bag", "shirt", "shoes",
    "jacket", "hat", "watch", "mirror", "comb", "bed", "pillow",

    "river", "mountain", "forest", "desert", "island", "ocean", "cloud",
    "rain", "storm", "snow", "fire", "stone", "rock", "sand", "tree", "leaf",
    "flower", "grass", "field", "village", "city", "road", "bridge", "school",
    "college", "market", "temple", "church", "castle", "palace", "garden"
]


hangman = {0:("   ","   ","   "),
           1:(" o ","   ","   "),
           2:(" o "," | ","   "),
           3:(" o ","/| ","   "),
           4:(" o ","/|\\","   "),
           5:(" o ","/|\\","/  "),
           6:(" o ","/|\\","/ \\")}
              
word = random.choice(words)
guessed = ['_']*len(word)
wrong_guesses = 0

print("_____________________________")
print("      WELCOME TO HANGMAN      ")
print("_____________________________")

while wrong_guesses < 6 and "_" in guessed:
    guess = input("Enter a letter:")

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input!")
        continue

    if guess in guessed:
        print("Letter already guessed!")
        wrong_guesses +=1
        print("_____________________________")
        print("___")
        print(" |")
        for i in hangman[wrong_guesses]:
            print(i)
        print("_____________________________")
        continue

    if guess in word:
        for letter in range(len(word)):
            if word[letter] == guess:
                guessed[letter] = guess
    
    for i in guessed:
        print(i, end=" ")
    print("")

    if guess not in word:
        wrong_guesses +=1
        print(f"You have {wrong_guesses} wrong guesses!")

    print("_____________________________")
    print("___")
    print(" |")
    for i in hangman[wrong_guesses]:
        print(i)
    print("_____________________________")

if not "_" in guessed:
    print("You won!") 
else:
    print("You died!")
print("_____________________________")