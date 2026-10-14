a = [4,8,2,9,11,10]
largest = a[0]
sec_largest = a[0]

for i in a:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
print(f"Your second largest is {sec_largest}")