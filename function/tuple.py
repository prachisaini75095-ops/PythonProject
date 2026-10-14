# a = ["Monday","Tuesday",123,876,123,123,123]
# tup = tuple(a)
# # print(type(tup))
# print(tup[-2])
# # it has unmutuable nature - you cannot change any values inside your tuple
# print(tup.index("Tuesday"))
# print(tup.count(123))

def student():
    return "prachi",19,"prachisddiet@gmail.com"

info = student()
name, age, mail = info
print(info)