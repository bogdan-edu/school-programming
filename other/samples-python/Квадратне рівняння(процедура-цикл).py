print("Розв'язок квадратного рівняння ax2+bx+c=0")


def quadkor():
    a = float(input("Введіть коефіцієнт a="))
    b = float(input("Введіть коефіцієнт b="))
    c = float(input("Введіть коефіцієнт c="))
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("Дискримінант більше нуля, рівняння має два корені:")
        print("x1=", x1)
        print("x2=", x2)
    elif d == 0:
        x = -b / (2 * a)
        print("Дискримінант дорівнює нулю, рівняння має один корінь:")
        print("x=", x)
    else:
        print("Дискримінант менше нуля, рівняння дійсних коренів не має")


prodovzhyty = "yes"
while prodovzhyty == "yes":
    quadkor()
    prodovzhyty = input("Якщо хочете розв'язати рівняння - введіть yes, для виходу натисныть клавішу ENTER ")
