import random


def bones():
    qube1 = random.randint(1, 6)
    qube2 = random.randint(1, 6)
    return qube1 + qube2


def winners(*points):
    win_points = max(points)
    winner = []
    for i in range(len(points)):
        if points[i] == win_points:
            person = 'Гравець-' + str(i+1)
            winner.append(person)
    return winner
