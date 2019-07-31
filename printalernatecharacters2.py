s1 = input("Enter the first String")
s2 = input("Enter The Second String")
s3 = ''
l1 = len(s1)
l2 = len(s2)
n = min(l1,l2)
for i in range(n):
    s3 += s1[i] + s2[i]
if l1>l2:
    s3+= s1[n:l1]
else:
    s3+= s2[n:l2]
print(s3)

