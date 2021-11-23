import random

new_list = [random.randint(1, 10) for _ in range(20)]

print(new_list)

bogdan_list = []
for el in new_list:
    if el % 2 != 0:
        bogdan_list.append(el)

print(bogdan_list)