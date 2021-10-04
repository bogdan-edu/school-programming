a = float(input('Введіть число: '))
n = int(input('Введіть степінь числа: '))
i = 1
result = 1
while i <= n:
    result = result * a
    i = i + 1

print('x в степені n: ', result)