# a = [1,2,2,3,4,4,5,6,6,7]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a.remove(2)
# print(a)
arr = [10, 20, 10, 30, 20, 40, 30]

arr.sort()

i = 0
while i < len(arr) - 1:
    if arr[i] == arr[i + 1]:
        arr.pop(i + 1)
    else:
        i += 1

print("Array after removing duplicates:", arr)