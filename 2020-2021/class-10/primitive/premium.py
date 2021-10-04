summ = input('Введіть оклад працівника: ')
prem = input('Якщо є премія, введіть "yes", якщо ні натисніть "Enter": ')
summ = float(summ)
if prem == 'yes':
    summ = summ * 1.5
else:
    sum = summ * 1.05
print('Зарплата працівника: ', summ, ' грн.')
