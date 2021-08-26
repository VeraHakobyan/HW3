number = int(input())

while number > 0:
    if number < 10:
        print('boring')
        break
    elif (number % 10) != ((number // 10) % 10):
        print('interesting')
        break
    else:
        number = number // 10
