from random import randint


class Qubes:
    def __init__(self, nq):
        self.quantity = nq
        self.points = []

    def game(self):
        for i in range(self.quantity):
            self.points.append(randint(1, 6))


class User:
    def __init__(self, nm):
        self.name = nm

