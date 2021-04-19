n = int(input('n =  '))
k = int(input('n =  '))
m = int(input('m =  '))
sn = 0
for i in range(1, n + 1):
    sn = sn + i

sk = 0
for i in range(1, k + 1):
    sk = sk + i

sm = 0
for i in range(1, m + 1):
    sm = sm + i

y = sn * sm / sk

print('y = ', y)
