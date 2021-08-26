number = int(input())

while number > 0:
    if number < 10:
        print('No')
        break
    elif number % 10 > (number // 10) % 10:
        print('Yes')
        break
    else:
        number = number // 10
