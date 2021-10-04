n = int(input('Для скількох чисел потрібно порахувати середнє значення? '))

s = 0
for i in range(n):
    s = s + float(input('Введіть число: '))
mid_val = s / n
print('Середнє значення введених чисел: ', mid_val)