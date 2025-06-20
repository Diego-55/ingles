import unittest
from building import Building

class TestBuilding(unittest.TestCase):
    def test_building_creation(self):
        b = Building("Principal")
        self.assertEqual(b.name, "Principal")
        self.assertEqual(b.rooms, [])
        self.assertEqual(b.subbuildings, [])

    def test_count_all_rooms(self):
        # Jerarquía: edificio -> sub1, sub2; sub1 -> sub3
        sub3 = Building("Sub3", rooms=["R5", "R6"])
        sub1 = Building("Sub1", rooms=["R3"], subbuildings=[sub3])
        sub2 = Building("Sub2", rooms=["R4"])
        edificio = Building("Principal", rooms=["R1", "R2"], subbuildings=[sub1, sub2])
        self.assertEqual(edificio.count_all_rooms(), 6)
        self.assertEqual(sub1.count_all_rooms(), 3)
        self.assertEqual(sub2.count_all_rooms(), 1)
        self.assertEqual(sub3.count_all_rooms(), 2)

if __name__ == "__main__":
    unittest.main()