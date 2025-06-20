import unittest
from course import Course

class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        c = Course("Inglés Básico")
        self.assertEqual(c.name, "Inglés Básico")
        self.assertEqual(c.subcourses, [])

    def test_count_all_subcourses(self):
        # Jerarquía: curso -> sub1, sub2; sub1 -> sub3
        sub3 = Course("Subcurso 3")
        sub1 = Course("Subcurso 1", [sub3])
        sub2 = Course("Subcurso 2")
        curso = Course("Curso Principal", [sub1, sub2])
        self.assertEqual(curso.count_all_subcourses(), 3)
        self.assertEqual(sub1.count_all_subcourses(), 1)
        self.assertEqual(sub2.count_all_subcourses(), 0)
        self.assertEqual(sub3.count_all_subcourses(), 0)

if __name__ == "__main__":
    unittest.main()