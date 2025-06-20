class Room:
    def __init__(self, number, subrooms=None):
        self.number = number
        self.subrooms = subrooms if subrooms else []

    # Método recursivo para contar todas las habitaciones (incluyendo subhabitaciones)
    def count_all_rooms(self):
        count = 1  # Cuenta esta habitación
        for sub in self.subrooms:
            if isinstance(sub, Room):
                count += sub.count_all_rooms()
        return count