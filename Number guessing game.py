import random
correct_number = random.randint(0,9)
print("You will get three attempts")
number_of_tries = 1
while number_of_tries<=3:
    ask_user = int(input("Enter the number :\t "))
    if ask_user == correct_number:
        print("You have guessed it right")
    else:
        print("Wromg guess \nNext attempt ")

    number_of_tries = number_of_tries+1


print("You have crossed the limit!!!!")