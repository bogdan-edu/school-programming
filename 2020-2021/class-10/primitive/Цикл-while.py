print("Сума чисел від 1 до n")
n = int(input("введіть число n = "))
summ = 0
count = 1
while count <= n:
    summ = summ + count
    count = count + 1
    print(summ)
print("Сума чисел від 1 до n дорівнює ", summ)
