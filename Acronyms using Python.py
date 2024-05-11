ask_user = input("Enter your sentence : \t")
text = ask_user.split(" ")
AC = ""
for a in text:
    AC=AC+a[0]
print(AC)