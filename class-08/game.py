import random
x = random.randint(1, 4)
y = input('Вгадай число від 1 до 4: ')
y = int(y)
if x == y:
    print('Вгадав')
else:
    print('Не вгадав, я  загадував: ', x)