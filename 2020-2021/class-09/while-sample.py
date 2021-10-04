password = '123456789'

user_password = input('Введіть пароль: ')

count = 1
while password == user_password:
    user_password = input('Пароль не правильний. Введіть пароль: ')
    if count > 3: continue
#    user_password = input('Пароль не правильний. Введіть пароль: ')
    count = count + 1

print('Пароль правильний, ви його ввели з ', count, ' разу')
print('А тут у нас виконується основна програма')
