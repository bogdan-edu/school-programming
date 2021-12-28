def long(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def is_rectangular(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        return True
    elif b ** 2 == a ** 2 + c ** 2:
        return True
    elif c ** 2 == a ** 2 + b ** 2:
        return True
    else:
        return False


xa = int(input('Введіть координату x вершини А: '))
ya = int(input('Введіть координату y вершини A: '))
xb = int(input('Введіть координату x вершини B: '))
yb = int(input('Введіть координату y вершини B: '))
xc = int(input('Введіть координату x вершини C: '))
yc = int(input('Введіть координату y вершини C: '))

node_a = xa, ya
node_b = xb, yb
node_c = xc, yc

side_a = long(node_b, node_c)
side_b = long(node_a, node_c)
side_c = long(node_a, node_b)

if is_rectangular(side_a, side_b, side_c):
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} є прямокутним')
else:
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} не є прямокутним')
