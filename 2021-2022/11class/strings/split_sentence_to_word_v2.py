sentence = input('Введіть речення: ')

for s in ',.:;!?-"':
    sentence = sentence.replace(s, '')

words = sentence.split(' ')
for word in words:
    print(word)
