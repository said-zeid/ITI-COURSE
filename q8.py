def is_even(list1):
    list3 = []
    for x in list1:
        if x % 2 == 0:
            list3.append(x)
    return list3


list2 = [1, 2, 3, 4]
l = is_even(list2)
print(l)
