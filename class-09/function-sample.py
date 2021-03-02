def hello1(name):
    n = len(name)
    return str(name) + ' , в твоєму імені ' + str(n) + ' букв'
    print('Я б щось написав, але вище мене return')

def hello2(name):
    n = len(name)
    print( name, ' , в твоєму імені ', n, ' букв')


print(hello1('Марфа'))


hello2('Йосип')
