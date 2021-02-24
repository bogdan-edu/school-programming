# функція визначення довжини відрізка
def vidrizok(ax, ay, bx, by):
    if ax > bx:
        abx = ax - bx
    else:
        abx = bx - ax

    if ay > by:
        aby = ay - by
    else:
        aby = by - ay
    result = (abx ** 2 + aby ** 2) ** 0.5
    return result


# основна програма
# запитуємо у користувача координати вершин
xa = float(input('Введіть координату X точки A: '))
ya = float(input('Введіть координату y точки A: '))
xb = float(input('Введіть координату X точки B: '))
yb = float(input('Введіть координату Y точки B: '))
xc = float(input('Введіть координату X точки С: '))
yc = float(input('Введіть координату Y точки С: '))
xd = float(input('Введіть координату X точки D: '))
yd = float(input('Введіть координату Y точки D: '))
# обчислюємо сторони трикутника
ab = vidrizok(xa, ya, xb, yb)
bc = vidrizok(xa, ya, xb, yb)
cd = vidrizok(xc, yc, xd, yd)
ad = vidrizok(xa, ya, xd, yd)
# Обчислюємо периметр
p = ab + bc + cd + ad
# Виводимо на екран значення периметра
print('Периметр трикутника:', p)
