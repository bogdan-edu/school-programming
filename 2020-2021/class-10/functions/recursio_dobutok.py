def dobutok(x, y):
    if y == 0:
        return 0
    else:
        return dobutok(x, y - 1) + x


a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: : '))
result = dobutok(a, b)
print('добуток чисел: ', result)
