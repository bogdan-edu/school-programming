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

perimeter = long(node_a, node_b) + long(node_a, node_c) + long(node_b, node_c)

print(f'Периметр трикутника з вершинами {node_a}, {node_b}, {node_c} дорівнює {perimeter}')
