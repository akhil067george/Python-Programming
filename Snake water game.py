import random
your_score = 0
system_score = 0
'''
Snake = 0
Water = 1
Gun = 2
'''
number_of_tries = 1
while number_of_tries <=3:
    a = int(input("Enter the input of your choice, Snake = 0, Water = 1, Gun = 2 : \t"))
    print("Your choice", a)
    b = random.randint(0, 2)
    print("System choice", b)
    if a == 0:
        if b == 1:
            your_score = your_score+1
            system_score = 0
        elif b ==2:
            system_score = system_score+1
            your_score = 0
    elif a == 1:
        if b == 2:
            your_score = your_score + 1
            system_score = 0
        elif b == 0:
            system_score = system_score + 1
            your_score = 0
    elif a == 2:
        if b == 0:
            your_score = your_score + 1
            system_score = 0
        elif b == 1:
            system_score = system_score + 1
            your_score = 0
    else:
        system_score = 0
        your_score = 0

    number_of_tries = number_of_tries+1

print("You scored", your_score)
print("System scored", system_score)

if system_score>your_score:
    print("Winner is Akhil")

else:
    print("Winner is System")





