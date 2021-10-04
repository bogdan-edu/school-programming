num = input('На яке число нам треба табличка множення? ')
num = int(num)
for i in range(1, 10):
    dob = i * num
    print(i, 'x', num, '=', dob)