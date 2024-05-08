import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
characters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '+']

a = int(input("How many alphabets you want ? \t"))
b = int(input("How many numbers you want ? \t"))
c = int(input("How many characters you want ? \t"))

pass_generated = ""

for i in range(1, a+1):
    pass_generated = pass_generated + random.choice(alphabets)

for x in range(1, b+1):
    pass_generated = pass_generated + random.choice(numbers)

for y in range(1, c+1):
    pass_generated = pass_generated + random.choice(characters)

print(f"Your password is : {pass_generated}")