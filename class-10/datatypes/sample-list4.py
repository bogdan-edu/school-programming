a = 'Богдан'
b = input('Введіть букву: ')
a_list = list(a)
if b in a_list:
    print('є така буква')
else:
    print('немає такої букви')