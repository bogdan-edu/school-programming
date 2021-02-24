import random

def qrandint(start, end):
    return random.randint(start, end) ** 2


a = qrandint(3, 7) + qrandint(3, 7) + qrandint(3, 7)
print(a)