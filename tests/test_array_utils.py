import unittest
from utils.array_utils import second_max, second_lowest_students, adjacent_nearest_neighbor

class TestArrayUtils(unittest.TestCase):
    def test_second_max(self):
        self.assertEqual(second_max([1, 2, 6, 6, 6, 5]), 5)  # Legacy bug verification
        self.assertEqual(second_max([10, 20]), 10)
        with self.assertRaises(ValueError):
            second_max([10])
        with self.assertRaises(ValueError):
            second_max([10, 10, 10])

    def test_second_lowest_students(self):
        # Legacy bug: sec_min_max.txt was completely syntax-broken
        students = [['harry', 38], ['berry', 39], ['cherry', 39], ['sherry', 40]]
        self.assertEqual(second_lowest_students(students), ['berry', 'cherry'])
        
        single_student = [['harry', 38]]
        with self.assertRaises(ValueError):
            second_lowest_students(single_student)
            
        same_grades = [['harry', 38], ['berry', 38]]
        with self.assertRaises(ValueError):
            second_lowest_students(same_grades)

    def test_adjacent_nearest_neighbor(self):
        lst = [1, 3, 5, 6, 8, 9]
        
        # Test middle element
        self.assertEqual(adjacent_nearest_neighbor(lst, 5), 6) # distances to 3 is 2, to 6 is 1 -> returns 6
        
        # Test boundary cases (Legacy bug: caused IndexError or negative wraparound)
        self.assertEqual(adjacent_nearest_neighbor(lst, 1), 3) # Leftmost boundary -> returns 3
        self.assertEqual(adjacent_nearest_neighbor(lst, 9), 8) # Rightmost boundary -> returns 8
        
        # Test value not in list error
        with self.assertRaises(ValueError):
            adjacent_nearest_neighbor(lst, 10)

if __name__ == "__main__":
    unittest.main()
