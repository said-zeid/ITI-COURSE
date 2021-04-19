l = []


def max(l):
    l.sort(reverse=True)
    print(l[0])


def min(l):
    l.sort()
    print(l[0])


try:
    x = 0
    while x < 10:
        s = input("enter a num ")
        if s == "done":
            max(l)
            min(l)
            break
        else:
            f = int(s)
            l.append(f)
            x = x + 1

except:
    print("Invalid input try again")
