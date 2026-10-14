temp = int(input("Please tell temperature: "))
if(temp >= -5 and temp <= 5):
    print("Very cold")
elif(temp >= 6 and temp <= 18):
    print("Cold")
elif(temp >= 19 and temp <= 30):
    print("Hot")
else:
    print("Very hot")
