s = (input("Enter The String:"))
alpha= []
digit = []
if s.isalnum():
    for i in range(len(s)):
        if s[i].isalpha():
            alpha.append(s[i])
        elif s[i].isdigit():
            digit.append((s[i]))
    alpha.sort()
    digit.sort()
    output = alpha + digit
    print(output)
else: print("Please Enter onlt alphabets and digits:")




