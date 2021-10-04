import random

x = random.randint(1, 10)
y = int(input('Вгадай число від 1 до 10: '))

i = 1
while x != y:
    y = int(input('Не вгадав, спробуй ще : '))
    i = i + 1

print('Вгадав з ', i, ' разу' )