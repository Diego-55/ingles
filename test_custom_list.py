import unittest
from custom_list import CustomList

class TestCustomList(unittest.TestCase):
    def test_recursive_sum(self):
        cl = CustomList([1, 2, 3])
        self.assertEqual(cl.recursive_sum(), 6)

    def test_add(self):
        cl = CustomList()
        cl.add(5)
        self.assertIn(5, cl.items)

if __name__ == "__main__":
    unittest.main()