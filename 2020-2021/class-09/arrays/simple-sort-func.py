import random


def randarray(value):
    random_array = []
    for k in range(value):
        random_array.append(random.randint(1, 100))
    return random_array


my_array = randarray(10)
print('my_array = ', my_array)
