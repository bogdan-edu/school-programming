import random


class Gamer:
    name = ''
    hits = 0

    def game(self, qubes):
        self.hits = 0
        for i in range(qubes):
            self.hits = self.hits + random.randint(1, 6)

n = int(input('Скільки кубиків у грі? '))
player1 = Gamer()
player2 = Gamer()

player1.name = input('Як звати першого гравця? ')
player2.name = input('Як звати другого гравця? ')


player1.game(n)
player2.game(n)

if player1.hits > player2.hits:
    print('Переміг ', player1.name)
elif player2.hits > player1.hits:
    print('Переміг ', player2.name)
else:
    print('Нічия')
print(player1.name, ' набрав очок: ', player1.hits)
print(player2.name, ' набрав очок: ', player2.hits)
