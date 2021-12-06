word = input('Введіть слово: ')
if word == word[::-1]:
    print(f'Слово {word} є паліндромом')
else:
    print(f'Слово {word} не є паліндромом')
