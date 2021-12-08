sentence = input('Введіть речення: ')
end_word = sentence.find(' ')
word = sentence[:end_word]
print('Перше слово: ', word)
