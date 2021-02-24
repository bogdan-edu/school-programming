import random

n = int(input('Скільки разів підкидаємо кубик?: '))
summ = 0
for i in range(n):
    summ = summ + random.randint(1, 6)
    print(summ)
mid = summ / n
print('Середнє значення за ', n, 'підкидань буде: ', mid)