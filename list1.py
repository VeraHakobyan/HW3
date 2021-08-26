n = int(input())

lst = []

for _ in range(n):
    lst.append(input())

sum_str = ''

for el in lst:
    sum_str += el

print(sum_str)
