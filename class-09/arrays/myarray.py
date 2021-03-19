import random

def randarray(value):
    random_array = []
    for i in range(value):
        random_array.append(random.randint(1, 1000))
    return random_array


def maxelem(value):
    m = value[0]
    for i in range(len(value)):
        if value[i] > m:
            m = value[i]
    return m

def minelem(value):
    m = value[0]
    for i in range(len(value)):
        if value[i] < m:
            m = value[i]
    return m
