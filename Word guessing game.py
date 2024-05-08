import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

correct_answer = random.choice(words)
print("You have three attempts ! \nAll the best!")
number_of_tries = 1
while number_of_tries<=3:
    ask_user = input("Enter your guess : \t")
    if ask_user == correct_answer:
        print("You have guessed it right!")
    else:
        print("Next attempt")
        number_of_tries = number_of_tries+1

print("You have crossed the limit!!!!")