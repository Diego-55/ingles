class Building:
    def __init__(self, name, rooms=None, subbuildings=None):
        self.name = name
        self.rooms = rooms if rooms else []
        self.subbuildings = subbuildings if subbuildings else []

    def add_room(self, room):
        self.rooms.append(room)

    def add_subbuilding(self, subbuilding):
        self.subbuildings.append(subbuilding)

    # Método recursivo para contar todas las habitaciones en este edificio y subedificios
    def count_all_rooms(self):
        count = len(self.rooms)
        for sub in self.subbuildings:
            if isinstance(sub, Building):
                count += sub.count_all_rooms()
        return count