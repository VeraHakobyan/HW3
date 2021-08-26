n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

minimum1 = lst[0]
minimum2 = lst[1]


for el in lst:
    if el < minimum1 and el < minimum2:
        minimum2 = minimum1
        minimum1 = el
    elif minimum2 > el > minimum1:
        minimum2 = el

print(minimum2)
