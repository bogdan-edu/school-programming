alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
chars = ',.;:`''"+-*<>=![]{}()?%'

word = input('Введіть слово для перевірки: ')
word = list(word)

for i in range(len(word)):
    if word[i] in alphabet:
        print(i + 1, '-й символ ok')
    elif word[i] == ' ':
        print(i + 1, '-й символ "пробіл"')
    elif word[i] in chars:
        print(i + 1, '-й символ є розділовим знаком')
    else:
        print(i + 1, '-й символ не є буквою англійського алфавіту')
