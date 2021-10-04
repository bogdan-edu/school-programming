x = input('Введи слово: ')
y = input('Введи букву: ')

z = list(x)
if y in z:
    print('Є така буква в слові')
else:
    print('Немає такої букви в слові')