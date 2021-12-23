# import math
from math import sqrt

node_a = 1, 1
node_b = 4, 5


def long(a, b):
    # return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


print(long(node_a, node_b))
