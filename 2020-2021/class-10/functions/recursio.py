def recursio_func(x, i):
    if i == 0:
        return 1
    else:
        return recursio_func(x, i - 1) * x


a = float(input('Введіть число: '))
n = int(input('Введіть степінь числа: '))
result = recursio_func(a, n)
print('x в степені n: ', result)
