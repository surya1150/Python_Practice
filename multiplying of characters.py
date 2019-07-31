s = input("Enter the String as character followed by digit:")
result= ''
i = 0
while True:
    if i < len(s):
        if s[i].isalpha():
            if s[i+1].isdigit():
                result+= s[i] * int(s[i+1])
        i = i+2
    else : break
print(result)


