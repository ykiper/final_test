from .soldier import Soldier

class Room:

    available_place = 8

    def __init__(self, room_number: int):
        self.room_number: int = room_number
        self.soldiers_list: list[Soldier] = []


    def assign_to_room(self, soldier: Soldier):
        if Room.available_place > 0:
            self.soldiers_list.append(soldier)
            Room.available_place -= 1
            return True
        return False

    def __repr__(self):
        return f"room number: {self.room_number}, soldiers list: {self.soldiers_list},\n"