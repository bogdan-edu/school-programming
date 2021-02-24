print("Знаходження коренів квадратного рівняння ax^2+bx+c=0")

a = float(input("Введіть коефіцієнт a = "))
b = float(input("Введіть коефіцієнт b = "))
c = float(input("Введіть коефіцієнт c = "))


def koren_quadrat():
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        print("Дискримінант більше нуля D = ", d, " > 0")
        print("Рівняння має два дійсних корені:")
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif d == 0:
        x12 = -b / (2 * a)
        print("Дискримінант дорівнює нулю D = ", d)
        print("Рівняння має один дійсний корінь:")
        print("x = ", x12)
    else:
        print("Дискримінант менше нуля D = ", d, " < 0")
        print("Рівняння дійсних коренів не має")


def koren_line():
    x = -c / b
    print("Рівняння є лінійним та має один корінь x = ", x)


if a == 0 and b != 0:
    koren_line()
elif a == 0 and b == 0:
    print("Данний вираз не є рівнянням")
else:
    koren_quadrat()
