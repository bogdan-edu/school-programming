a = float(input('введіть коефіцієнт a = '))
b = float(input('введіть коефіцієнт b = '))
c = float(input('введіть коефіцієнт c = '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / 2 * a
    x2 = (-b - d ** 0.5) / 2 * a
    print('x1 = ', x1)
    print('x2 = ', x2)
elif d == 0:
    x = -b / 2 * a
    print('x = ', x)
else:
    print('Рівняння дійсних коренів немає')
