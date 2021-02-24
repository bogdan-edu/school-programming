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
    result = (abx**2 + aby**2)**0.5
    return result
# основна програма
xa = float(input('Введіть координату X точки A: '))
xb = float(input('Введіть координату X точки B: '))
ya = float(input('Введіть координату y точки A: '))
yb = float(input('Введіть координату Y точки B: '))
t = float(input('Введіть час руху між точками: '))

