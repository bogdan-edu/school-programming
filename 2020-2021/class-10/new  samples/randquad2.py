import random

def qrandint(start, end, n):
    s = 0
    for i in range(n):
        s = s + random.randint(start, end) ** 2
    return s

print(qrandint(1, 7, 4))