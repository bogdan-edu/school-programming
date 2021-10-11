from random import randint

random_numbers = [randint(1, 10) for _ in range(20)]
print(random_numbers)

# variant 1
print('Var1')
for number in random_numbers:
    print(number)

# variant 2
print('Var2')
for i in range(len(random_numbers)):
    print(random_numbers[i])