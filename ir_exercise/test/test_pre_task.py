import unittest


class StudentIDTest(unittest.TestCase):
    def test_student_id_filled(self):
        student_id = "12216472"
        self.assertNotEqual(student_id, "")
        with open("student_id.txt", "wt") as f:
            f.write(f"{student_id}")


if __name__ == "__main__":
    unittest.main()
