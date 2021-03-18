name = input('Як тебе звати? ')
suma = input('Скільки в тебе грошей? ')
suma = int(suma)

if suma == 10000:
    print(name, ', ти можеш купити що хочеш')
elif suma > 10000:
    print(name, ', ти можеш купити що хочеш і в тебе ще залишиться на цукерки')
else:
    print(name, ', іди працюй')