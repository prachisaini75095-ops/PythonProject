a = int(input("Tell your number : "))
copy = a
rev = 0
while a>0:
    rev = rev*10 + a%10
    a = a // 10
if rev == copy:
    print("Palindrome")
else:
    print(" not a palindrome")