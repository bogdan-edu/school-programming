alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'
char = input('введіть букву для перевірки: ')
if char in alphabet:
    print('символ ok')
else:
    print('символ не є буквою англійського алфавіту')
