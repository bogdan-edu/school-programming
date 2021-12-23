node_a = 1, 1
node_b = 4, 5


def long(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


print(long(node_a, node_a))
