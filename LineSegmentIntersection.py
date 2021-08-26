a1 = float(input())
b1 = float(input())
lst1 = [a1, b1]
lst1.sort()

a2 = float(input())
b2 = float(input())
lst2 = [a2, b2]
lst2.sort()

if lst1[0] < lst2[0]:
    if lst2[1] > lst1[1] > lst2[0]:
        print(lst1[1] - lst2[0])
    elif lst1[1] > lst2[1]:
        print(lst2[1] - lst2[0])
    else:
        print(0)

else:
    if lst1[1] > lst2[1] > lst1[0]:
        print(lst2[1] - lst1[0])
    elif lst2[1] > lst1[1]:
        print(lst1[1] - lst1[0])
    else:
        print(0)



