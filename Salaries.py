salary1 = int(input())
salary2 = int(input())
salary3 = int(input())

if salary1 >= salary2 and salary1 >= salary3:
    if salary2 >= salary3:
        print(salary1 - salary3)
    else:
        print(salary1 - salary2)

elif salary2 >= salary3:
    if salary1 >= salary3:
        print(salary2 - salary3)
    else:
        print(salary2 - salary1)

else:
    if salary1 >= salary2:
        print(salary3 - salary2)
    else:
        print(salary3 - salary1)
