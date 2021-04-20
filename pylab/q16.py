s = input("enter the file name ")

f = open(s)
count = 0
for x in f:
    l = x.split()
    for j in l:
        if j == "From":
            count = count+1
            for z in l:
                if z == "From":
                    continue
                print(z)
                break

print("the count = "+str(count))

f.close()
