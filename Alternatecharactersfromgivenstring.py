s1 = input("Enter First String:")
s2 = input("Enter Second String")
s3 = ''

if len(s1) ==  len(s2):
    for i in range(len(s1)):
        s3 = s3 + s1[i] + s2[i]
    print (s3)
elif len(s1)>len(s2):
    for i in range(len(s1)):
        if i < len(s2):
            s3 = s3 + s1[i] + s2[i]
        else:
            s3 = s3 + s1[i]
    print(s3)
elif len(s2)>len(s1):
    for i in range(len(s2)):
        if i < len(s1):
            s3 = s3 + s1[i] + s2[i]
        else:
            s3 = s3 + s2[i]
    print (s3)

