import random


def bones():
    qube1 = random.randint(1, 6)
    qube2 = random.randint(1, 6)
    points = qube1 + qube2
    return [points, qube1, qube2]


gamer1 = bones()
gamer2 = bones()


if gamer1[0] > gamer2[0]:
    print('Переміг перший гравець')
elif gamer2[0] > gamer1[0]:
    print('Переміг другий гравець')
else:
    print('Нічия')

print('Перший гравець набрав ', gamer1[0], ' очок')
print('Другий гравець набрав ', gamer2[0], ' очок')
