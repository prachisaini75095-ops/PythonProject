# a = int(input("Tell your number : "))
# while a>0:
#     print(a%10)
#     a = a // 10

# FOR ONE LINE
a = int(input("Tell your number : "))
rev = 0
while a>0:
    rev = rev*10 + a%10
    a = a // 10

print(rev)
