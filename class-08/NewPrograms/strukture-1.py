def suma(x):
    s = 0
    for i in range(1, x + 1):
        s = s + i
    return s


n = int(input('n =  '))
k = int(input('k =  '))
m = int(input('m =  '))
y = suma(n) * suma(m) / suma(k)
print('y = ', y)
