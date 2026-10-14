a = [20,43,17,68,27,90,47]
largest = a[0]
index = 0
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i
print(f"Your largest value is {largest} at index {index}")

