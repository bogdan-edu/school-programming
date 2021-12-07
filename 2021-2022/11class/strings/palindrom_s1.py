sentence = input('Введіть речення: ')
sentence = sentence.lower()

for s in ' ,.:;!?-"':
    sentence = sentence.replace(s, '')

if sentence == sentence[::-1]:
    print('Речення є паліндромом')
else:
    print('Речення не є паліндромом')


