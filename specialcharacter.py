a = "p@#yn26at8&i5ve"
char = 0
spchar = 0
digits = 0
for i in a:
    if(ord(i) >= 65 and ord(i) <= 90)or(ord(i) >= 97 and ord(i) <= 122):
        char += 1
    elif ord(i) >= 48 and ord(i) <= 90 :
        digits += 1
    else:
        spchar = spchar + 1

print(f"characters: {char}, special characters: {spchar}, digits: {digits}")
       