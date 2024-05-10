import random
chance = 1
correct_answer = random.randrange(1000,10000)
print(correct_answer)
while chance<=5:
    correct = ['_']*4
    right_digits = 0
    print("Guess a 4 digit number of your choice ")
    ask_user = int(input("Enter the number: \t"))
    if correct_answer==ask_user:
        print("Awesome ! You have cracked in one go !")
        break
    else:
        ask_user=str(ask_user)
        correct_answer=str(correct_answer)
        for i in range(0,4):
            if ask_user[i]==correct_answer[i]:
                right_digits=right_digits+1
                correct[i] = ask_user[i]

        if right_digits == 4:
            print("Congrats!")
            break

        print(f"You have guessed {right_digits} digits correctly out of 4")
        print("Current status ", correct)

    chance = chance+1