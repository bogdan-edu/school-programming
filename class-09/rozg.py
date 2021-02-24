age = input('Скільки тобі років? ')
age = float(age)
if age < 6:
    print('Іди в садочок')
elif age < 17:
    print('Іди в школу')
    if age > 16:
        print('Готуйся до ЗНО')
    else:
        print('ЗНО в тебе як мінімум через рік')
        if age == 16:
            print('Тобі рівно 16 років')
elif age < 65:
    print('Іди працюй')
else:
    print('Сиди на пенсії')
print('Бувай здоровий')
