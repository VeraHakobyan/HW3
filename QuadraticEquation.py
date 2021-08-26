import math

a, b, c = float(input()), float(input()), float(input())
D = int(b ** 2 - 4 * a * c)

if a != 0:
    print('Quadratic equation')
    print('Discriminant: {}'.format(D))
    if D > 0:
        x1 = (-b + math.sqrt(D)) / 2 * a
        x2 = (-b - math.sqrt(D)) / 2 * a
        print('Two solutions: {} {}'.format(x1, x2))
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / 2 * a
        print('One solution: {}'.format(x1))
    else:
        print('No solutions')
elif a == 0 and b != 0:
    print('Non-quadratic equation')
    x1 = -c / b
    print('One solution: {}'.format(x1))
elif a == 0 and b == 0 and c != 0:
    print('Non-quadratic equation')
    print('No solutions')
else:
    print('Non-quadratic equation')
    print('Infinite solutions')
