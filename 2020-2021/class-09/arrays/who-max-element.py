import random

# Задаємо масив випадкових чисел
n = int(input('Скільки елементів масиву має бути? '))

random_numbers = []
for i in range(n):
    random_numbers.append(random.randint(1, 10))

print(random_numbers)

# Шукаємо найбільший елемент масиву
max_element = random_numbers[0]
index = 0
for i in range(len(random_numbers)):
    if random_numbers[i] > max_element:
        max_element = random_numbers[i]
        index = i

print('Найбільший елемент = ', max_element)
print('Порядковий номер найбільшого елемента', index)