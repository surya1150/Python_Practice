vowels = ['a','e','i','o','u']
words = input("Enter The word:")

found =[]

for w in words:
    if w in vowels:
        if w not in found:
            found.append(w)
print(found)