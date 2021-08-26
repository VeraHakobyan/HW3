x = int(input())
divisors = 0

for i in range(x, 0, -1):
    if x % i == 0:
        divisors += 1

print(divisors)
