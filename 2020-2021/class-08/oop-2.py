class People:
    def __init__(self, x='', y=0, z='десь'):
        self.name = x
        self.age = y
        self.address = z

    def hello(self):
        phrase = 'Привіт, мене звати ' + self.name + ', мені ' + str(self.age) + ' років, '
        print(phrase)

    def friend(self):
        print('Мене звати', self.name, 'я дружу з ', bodya.name)



girl = People('Настя', 15)
boy = People('Хлопчик')
bodya = People('Бодя', 40, 'Велика Багачка')

boy.hello()
bodya.hello()
girl.hello()

boy.friend()
bodya.friend()
girl.friend()

print(bodya.address)
