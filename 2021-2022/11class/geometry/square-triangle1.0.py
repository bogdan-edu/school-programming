def long(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


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

if side_a ** 2 == side_b ** 2 + side_c ** 2:
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} є прямокутним')
elif side_b ** 2 == side_a ** 2 + side_c ** 2:
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} є прямокутним')
elif side_c ** 2 == side_a ** 2 + side_b ** 2:
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} є прямокутним')
else:
    print(f'Трикутник з вершинами {node_a}, {node_b}, {node_c} не є прямокутним')
