A = 1, 1
B = 4, 5


def long(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


print(long(A, B))
