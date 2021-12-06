sentence = input('Введіть речення: ')
sentence = sentence.lower()
sentence = sentence.replace(' ', '')
if sentence == sentence[::-1]:
    print('Речення є паліндромом')
else:
    print('Речення не є паліндромом')
