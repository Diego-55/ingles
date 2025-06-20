import unittest
from room import Room

class TestRoom(unittest.TestCase):
    def test_count_all_rooms(self):
        # Habitación principal con 2 subhabitaciones, una de ellas con otra subhabitación
        subsub = Room(104)
        sub1 = Room(102, [subsub])
        sub2 = Room(103)
        principal = Room(101, [sub1, sub2])
        self.assertEqual(principal.count_all_rooms(), 4)
        self.assertEqual(sub1.count_all_rooms(), 2)
        self.assertEqual(sub2.count_all_rooms(), 1)
        self.assertEqual(subsub.count_all_rooms(), 1)

if __name__ == "__main__":
    unittest.main()