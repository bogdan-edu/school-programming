def midvalue(*values):
    s = 0
    for i in values:
        s = s + i
    return s / len(values)


x = midvalue(1, 5, 13, 48, 0, 5)
print(x)
