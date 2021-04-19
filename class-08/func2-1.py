def sumnum(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


z = (sumnum(5) * sumnum(10)) / (sumnum(40) * 5)
print(z)

