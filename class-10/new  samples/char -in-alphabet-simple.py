alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

word = input('Введіть слово для перевірки: ')
word = list(word)

for i in range(len(word)):
    if word[i] in alphabet:
        print(i + 1, '-й символ ok')
    else:
        print(i + 1, '-й символ не є буквою англійського алфавіту')
