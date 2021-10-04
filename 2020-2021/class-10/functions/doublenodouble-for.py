def doubleif(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


def nodoubleif(num):
    if num % 2 != 0:
        return 1
    else:
        return 0


n = int(input('Введіть число: '))
countDouble = 0
countNoDouble = 0
for i in range(1, n+1):
    countDouble = countDouble + doubleif(i)
    countNoDouble = countNoDouble + nodoubleif(i)
print('Кількість парних чисел: ', countDouble)
print('Кількість непарних чисел: ', countNoDouble)
