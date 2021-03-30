import random


def randarray(value):
    random_array = []
    for i in range(value):
        random_array.append(random.randint(1, 100))
    return random_array





my_array = randarray(10)
print('my_array = ', my_array)

sorted_aaray = []
m = my_array[0]
for i in range(len(my_array)):
    if my_array[i] < m:
        m = my_array[i]
sorted_aaray.append(m)