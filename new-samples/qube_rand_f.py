import random

n = int(input('Скільки разів підкидаємо кубик?: '))


def quberandsumm(count):
    summ = 0
    for i in range(count):
        summ = summ + random.randint(1, 6)
    return summ


mid = quberandsumm(n) / n
print('Середнє значення за ', n, 'підкидань буде: ', mid)
