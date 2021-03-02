import random


def bones():
    qube1 = random.randint(1, 6)
    qube2 = random.randint(1, 6)
    return qube1 + qube2


def winner(points1, points2):
    if points1 > points2:
        return 'Переміг перший гравець'
    elif points2 > points1:
        return 'Переміг другий гравець'
    else:
        return 'Нічия'

