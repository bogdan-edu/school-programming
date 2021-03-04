print("Сума чисел від 1 до n")
summ = 0
n = int(input("Введіть n = "))
for count in range(1, n + 1):
    summ = summ + count
print("Сума чисел від 1 до", n, "дорівнює ", summ)
