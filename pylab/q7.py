def myfunc(list1):
    sumx = 0
    for x in list1:
        sumx = sumx+x
    return sumx


list2 = [1, 2, 3, 4]
l = myfunc(list2)
print(l)
"""
list3 = [1, 2, 3]
for x in range(0, 3):
    # list3.append(int(input()))
    list3[x] = int(input())
    """
