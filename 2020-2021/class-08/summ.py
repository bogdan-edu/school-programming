def suma(num):
    summ = 0
    for i in range(1, num + 1):
        summ = summ + i
    return summ

x = (suma(10) + suma(20)) / suma(5)

print(x)