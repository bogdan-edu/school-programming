# функція визнвчення суми чисел від 1 до n
def suma(i):
    s = 0
    for count in range(1, i + 1):
        s = s + count
    return s


# функція визнвчення добутку чисел від 1 до n
def dobutok(i):
    d = 1
    for count in range(1, i + 1):
        d = d * count
    return d


# Основна програма
n = int(input("Введіть число n="))
x = dobutok(n) / suma(n)
print("Значення виразу (1*2...n)/(1+2...n)=", x)
