s = input("enter the file name ")

f = open(s)
m = f.read().upper()
print(m)
# f.close()


"""
with open("abo.txt") as file:
    print(file)
