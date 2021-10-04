age = input('Привіт, скільки тобі років: ')
age = int(age)
if age >= 18:
    print('Ти вже повнолітній')
elif age < 2:
    print('Ти грудничок')
elif age < 6:
    print('Ти ще зовсім малий')
else:
    print('Ти вже школяр')
print('Кінець')
