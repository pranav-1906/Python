ques = ("Which animal is orange and has black stripes?", "What is the the largest mammal?", "What is the fastest land animal?", "Which animal lays largest eggs?")

options = (('a. zebra','b. tiger','c. chimp','d. hyena'),
           ('a. elphant','b. dinosaur','c. whale','d. shark'),
           ('a. usain bolt','b. cheetah','c. jaguar','d. ferrari'),
           ('a. ostrich','b. penguin','c. anaconda','d. duck'))

ans = ('b','c','b','a')
guesses = []
score = 0
ques_num = 0

for question in ques:
    print('------------------------')
    print(question)
    for option in options[ques_num]:
        print(option)
    
    guess = input("enter the correct option: ").lower()
    guesses.append(guess)
    if guess == ans[ques_num]:
        score+=1
        print('correct!')
    else:
        print('incorrect!')
        print(f"{ans[ques_num]} is the correct answer!")
    ques_num+=1

print(f'\nyour score is {score}/4')