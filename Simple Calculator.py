a = int(input("First number : \t"))
b = int(input("Second number : \t"))
c = input("Enter the operator: \t")

if c in ('+', '*', '/', '%', '-', '//'):
    if c == '+':
        print(a+b)
    elif c == '*':
        print(a*b)
    elif c =='/':
        print(a/b)
    elif c == '%':
        print(a%b)
    elif c =='-':
        print(a-b)
    elif c =='//':
        print(a//b)
else:
    print("Invalid response")
