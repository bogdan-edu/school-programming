import random

# new_list = [random.randint(3,9) for _ in range(10)]

new_list = []
for i in range(10):
    new_list.append(random.randint(3,9))

print(new_list)

el = 6

if el in new_list:
    print('Шістка є')
else:
    print('Шістки нема')