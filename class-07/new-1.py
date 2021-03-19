name = input('Як тебе звати? ')
age = input('Скільки тобі років? ')
age = int(age)

if age > 17:
    print(name, ', ти вже закінчив школу')
elif age < 6:
    print(name, ', ти ти ще не пішов в школу')
else:
    print(name, ', ти ще ходиш в школу')