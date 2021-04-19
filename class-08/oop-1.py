class People:
    name = ''
    age = 0
    address = ''

    def hello(self):
        phrase = 'Привіт, мене звати ' + self.name + ', мені ' + str(self.age) + ' років'
        print(phrase)


girl = People()
girl.name = 'Настя'
girl.age = 15

boy = People()

girl.hello()
boy.hello()

bodya = People()
bodya.name = 'Бодя'
bodya.age = 40
bodya.address = 'Велика Бвгачка'

bodya.hello()
print(bodya.address)