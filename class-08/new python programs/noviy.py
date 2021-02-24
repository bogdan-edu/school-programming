import random

s = 0
for i in range(10):
    x = random.randint(1, 6)
    s = s + x
    print(x)

mid = s / 10
print('Середнє значення: ', mid)