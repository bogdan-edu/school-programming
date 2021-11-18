for i in range(10):
    print(i)

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

for i in range(1, 10):
    number = i * 7
    print(number)

for number in numbers:
    number *= 7
    print(number)

for number in numbers:
    if number != 0:
        number = number * 7
        print(number)


