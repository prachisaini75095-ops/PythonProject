n = int(input("Tell your number: "))
Evensum = 0
Oddsum = 0
for i in range(1, n+1):
    if(i%2==0):
        Evensum = Evensum + i
    else:
        Oddsum = Oddsum + i
print(f"The even sum is {Evensum} and the odd sum is {Oddsum}")
