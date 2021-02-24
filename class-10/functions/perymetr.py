# функція визначення довжини відрізка
def vidrizok(ax, ay, bx, by):
    result = (abx**2 + aby**2)**0.5
    return result

# основна програма
# запитуємо у користувача координати вершин
xa = float(input('Введіть координату X точки A: '))
ya = float(input('Введіть координату y точки A: '))
xb = float(input('Введіть координату X точки B: '))
yb = float(input('Введіть координату Y точки B: '))
xc = float(input('Введіть координату X точки С: '))
yc = float(input('Введіть координату Y точки С: '))
# обчислюємо сторони трикутника
ab = vidrizok(xa, ya, xb, yb)
ac = vidrizok(xa, ya, xc, yc)
bc = vidrizok(xb, yb, xc, yc)
# Обчислюємо периметр
p = ab + ac + bc
# Виводимо на екран значення периметра
print('Периметр трикутника:', p)