strA="abcEFG"
for i in strA:
    if i.islower():
        i=i.upper()
    else:
        i=i.lower()
    print(i,end=" ")