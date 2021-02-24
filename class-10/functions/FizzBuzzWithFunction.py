def fizzbuzz(a):
    if a % 5 == 0 and a % 3 == 0:
        result = 'FizzBuzz'
    elif a % 3 == 0:
        result = 'Fizz'
    elif a % 5 == 0:
        result = 'Buzz'
    else:
        result = a
    return result
for i in range(1, 101):
    print(fizzbuzz(i))