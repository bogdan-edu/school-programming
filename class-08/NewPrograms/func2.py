x = 5
y = 10
a = 40

sx = 1
for i in range(1, x + 1):
    sx = sx * i

sy = 1
for i in range(1, y + 1):
    sy = sy * i

sa = 1
for i in range(1, a + 1):
    sa = sa * i

z = (sy * sx) / (sa * 5)
print(z)
