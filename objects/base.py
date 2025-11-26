from objects.soldier import Soldier
from objects.room import Room
from objects.dorm import Dorm

class Base:
    def __init__(self):
        self.dormA: Dorm = Dorm()
        self.dormB: Dorm = Dorm()
        self.waiting_list: list[Soldier] = []


