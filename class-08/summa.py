n = input('До якого числа нам потрібна сума? ')
n = int(n)
s = 0
for i in range(1, n+1):
    s = s + i
    print('i = ', i, 's = ', s)
print('Сума чисел від 1 до ', n, ',буде ', s)
