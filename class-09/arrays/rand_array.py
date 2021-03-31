import random

n = int(input('Скільки елементів масиву має бути? '))

random_numbers = []
for i in range(n):
    random_numbers.append(random.randint(1, 10))

print(random_numbers)

summ = 0
for i in range(len(random_numbers)):
    summ = summ + random_numbers[i]

print('Сума елемнтів', summ)
