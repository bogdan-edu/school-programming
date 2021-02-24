import random

n = int(input('Введіть кількість підкидань кубика n = '))

summ = 0
for i in range(n):
    rand = random.randint(1, 6)
    summ = summ + rand
    print('На кубику випало число: ', rand)
mid_rand = summ / n
print('Середнє значення чисел, що випали: ', mid_rand)
