import random

secret_number = random.randint(1, 9)
print('Тобі потрібно вгадати число ;)')

user_number = 10
count = 0
while user_number != secret_number:
    user_number = input('Введи число від 1 до 9: ')
    user_number = int(user_number)
    if user_number != secret_number:
        print('Ти не вгадав!')
    count = count + 1
print('Ти вгадав з ', count, ' спроби')