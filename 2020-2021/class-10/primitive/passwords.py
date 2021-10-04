password = '12345'
while True:
    user_password = input('Введіть пароль: ')
    if password == user_password:
        break
    else:
        print('Failed password!')
print('Welcome!')

