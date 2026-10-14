def palindrome_checker(a):
    copy = a
    rev = 0
    while a>0:
        rev = rev*10 + a%10
        a = a // 10
    if copy == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome_checker(121)
palindrome_checker(324)
palindrome_checker(1221)