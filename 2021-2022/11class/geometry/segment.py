xa = int(input('Введіть координату x вершини А: '))
ya = int(input('Введіть координату y вершини B: '))
xb = int(input('Введіть координату x вершини А: '))
yb = int(input('Введіть координату y вершини B: '))

node_a = xa, ya
node_b = xb, yb


def long(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


print(f'Відстань між точками {node_a} та {node_b} дорівнює {long(node_a, node_b)}')
