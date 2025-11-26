


class Soldier:
    def __init__(self, personal_number: int, first_name: str, last_name: str, gender: str,
                 distance_by_km: float, is_assigned: bool):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.distance_by_km = distance_by_km
        self.is_assigned = is_assigned

    def __str__(self):
        return f"""
        personal_number: {self.personal_number}, first_name: {self.first_name}, 
        last name: {self.last_name}, 
        gender: {self.gender}, 
        distance_by_km: {self.distance_by_km}, 
        is_assigned: {self.is_assigned}
"""

# print(Soldier(123, "vf", "tr", "male", 23, False))