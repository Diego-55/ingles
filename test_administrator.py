import unittest
from administrator import Administrator

class TestAdministrator(unittest.TestCase):
    def test_admin_attributes(self):
        a = Administrator("Eva", "eva@mail.com", "A001")
        self.assertEqual(a.name, "Eva")
        self.assertEqual(a.email, "eva@mail.com")
        self.assertEqual(a.admin_id, "A001")
        self.assertEqual(a.get_role(), "Administrator")

    def test_count_all_subordinates(self):
        # Jerarquía: jefe -> sub1, sub2; sub1 -> sub3
        sub3 = Administrator("Sub3", "sub3@mail.com", "A004")
        sub1 = Administrator("Sub1", "sub1@mail.com", "A002", [sub3])
        sub2 = Administrator("Sub2", "sub2@mail.com", "A003")
        jefe = Administrator("Jefe", "jefe@mail.com", "A001", [sub1, sub2])
        self.assertEqual(jefe.count_all_subordinates(), 3)
        self.assertEqual(sub1.count_all_subordinates(), 1)
        self.assertEqual(sub2.count_all_subordinates(), 0)
        self.assertEqual(sub3.count_all_subordinates(), 0)

if __name__ == "__main__":
    unittest.main()