l = [3,-1,4,-5,9]
pos = []
neg = []
for i in l:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print(f"positive elements are{pos} and negative elements are{neg}")