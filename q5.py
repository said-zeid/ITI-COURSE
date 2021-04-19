s=input("enter any string to remove vowels ")
#vowels=('a','e','u')
for x in s.lower():
    if x =='a' or x=='e' or x=='u' or x=='i' or x=='o':
        s=s.replace(x,"")

print(s) 