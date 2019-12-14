s = input("Enter the string")
substr = input("Enter the string to find")

flag = False
pos = -1
n = len(s)
while True:
    pos= s.find(substr,pos+1,n)
    if pos == -1:
        break
    print("Found at positon",pos)
    flag = True
if flag == False:
    print("String not found")