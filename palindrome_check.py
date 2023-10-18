b = input("Enter a string: ")

b = b.lower()

d = b[::-1]

if b == d :
    print(b,"is a palindrome.")
else :
    print(b,"isn't a palindrome.")
