a = input('Введіть перше число: ')
b = input('Введіть друге число: ')
a = float(a)
b = float(b)
if a > b:
    print('Перше число більше другого')
elif b > a:
    print('Друге чило більше першого')
else:
    print('Числа однакові')