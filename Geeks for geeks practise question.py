# Given two strings A and B consisting of lowercase english characters. Find the characters that are not common in the two strings.
# Note :- Return the string in sorted order.

A = input("Enter the text : \t")
B = input("Enter the text : \t")
uncommon_char = []
uncommon_char2 = []

if set(A) == set(B):
    print(-1)
C=A+B

for i in C:
    if i not in A:
        uncommon_char.append(i)
    elif i not in B:
        uncommon_char.append(i)


for i in uncommon_char:
    if i not in uncommon_char2:
        uncommon_char2.append(i)


print("".join(sorted(uncommon_char2)))

#geeksforgeeks
#geeksquiz