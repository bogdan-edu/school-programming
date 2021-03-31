import random


def randarray(value):
    random_array = []
    for k in range(value):
        random_array.append(random.randint(1, 100))
    return random_array


my_array = randarray(10)
print('my_array = ', my_array)

sorted_array = []
m = my_array[0]
temp = my_array
index = 0
for j in range(len(my_array)):
    for i in range(len(temp)):
        if temp[i] < m:
            m = temp[i]
            index = i
    sorted_array.append(m)
#    temp.pop(index)
print(sorted_array)
