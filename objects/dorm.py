# from abc import ABC, abstractmethod
from .room import Room


class Dorm:
    def __init__(self):
        self.rooms: list[Room] = [Room(i) for i in range(1, 9)]

dorm = Dorm()
print(dorm.rooms)