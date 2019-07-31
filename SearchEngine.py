t = int(input("Enter the Number Of Test Cases"))
list = []
tmp = []
dict1 ={}
for i in range(t):
    if len(list)>0:list.pop()
    c = int(input("Enter the number of search string queries"))
    for j in range(c):
        tmp = input().split()
        count = 0
        if tmp[0] == 'top':
            dict = {}
            for i in list:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1
            for key in sorted(dict.keys()):
                dict1[key]=dict[key]
            print(dict1)
            for x in dict1:
                if count < (int(tmp[1])):
                    print(x)
                count +=1
        else:
            list.append(tmp[0])



