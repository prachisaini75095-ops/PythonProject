# d = {}
# print(type(d))

# there is no indexing in the dictionary,, there is a key value
d = {10:100,20:200,30:300,40:400}
# print(d[30])
# d[50] = 500 creating a new key value pair
# print(d[50])
# d[10] = 110 #updating a key value
# print(d[10])

# methods approach
p = d.fromkeys([10,20,30,50,70],50)
print(p)
