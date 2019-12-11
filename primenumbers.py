pm = []
np = []
for n in range(20,50):
    if n > 1:
        count = 0
        for i in range(2,n):
            if (n % i) == 0:
                count +=1
        if count == 0:
            pm.append(n)
        else:
            np.append(n)
print (pm)
print (np)
