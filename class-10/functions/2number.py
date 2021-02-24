def maxnumber(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

a = float(input('Введіть число1: '))
b = float(input('Введіть число2: '))
c = maxnumber(a, b)

print('більше число:', c)