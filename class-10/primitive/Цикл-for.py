print("Сума чисел від 1 до n")
n = int(input("введіть число n = "))
summ = 0
for count in range(1, n + 1):
    print('count = ', count)
    summ = summ + count
    print('summ = ',summ)
print("Сума чисел від 1 до n дорівнює ", summ)