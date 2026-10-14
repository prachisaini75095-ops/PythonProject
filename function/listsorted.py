a = [10,20,30,40,50,60]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")