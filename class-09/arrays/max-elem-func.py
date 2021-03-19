import myarray

# основна програма
n = int(input('Скільки елементів масиву має бути? '))
random_numbers = myarray.randarray(n)
print(random_numbers)

max_element = myarray.maxelem(random_numbers)
print('Максимальний елемент: ', max_element)

min_element = myarray.minelem(random_numbers)
print('Мінімальний елемент: ', min_element)

random_numbers = myarray.randarray(n+10)
print(random_numbers)

max_element = myarray.maxelem(random_numbers)
print('Максимальний елемент: ', max_element)

min_element = myarray.minelem(random_numbers)
print('Мінімальний елемент: ', min_element)
