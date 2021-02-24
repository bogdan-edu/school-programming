def dilennya(a, b):
    if b == 0:
        c = 'На нуль ділити не можна'
    else:
        c = a / b
    return c
x = dilennya(10, 0)
print(x)
