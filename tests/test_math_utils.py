import unittest
from utils.math_utils import (
    isprime, ispronic, cube, square, isArmstrong, ispositive,
    ispalindrome, factorial, isspecial, get_proper_divisors,
    isniven, isneon, ismagic, isevil, power, isdisarium, isperfect, fibonacci
)

class TestMathUtils(unittest.TestCase):
    def test_isprime(self):
        self.assertTrue(isprime(2))
        self.assertTrue(isprime(13))
        self.assertFalse(isprime(1))
        self.assertFalse(isprime(9))  # Legacy bug: classified 9 as prime
        self.assertFalse(isprime(0))
        self.assertFalse(isprime(-5))

    def test_ispronic(self):
        self.assertTrue(ispronic(0))   # 0 * 1 = 0
        self.assertTrue(ispronic(6))   # 2 * 3 = 6
        self.assertTrue(ispronic(12))  # 3 * 4 = 12
        self.assertFalse(ispronic(5))
        self.assertFalse(ispronic(-6))

    def test_cube_and_square(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(square(4), 16)
        self.assertEqual(cube(-2), -8)
        self.assertEqual(square(-3), 9)

    def test_is_armstrong(self):
        self.assertTrue(isArmstrong(153))   # 1^3 + 5^3 + 3^3 = 153
        self.assertTrue(isArmstrong(1634))  # 1^4 + 6^4 + 3^4 + 4^4 = 1634
        self.assertFalse(isArmstrong(10))
        self.assertFalse(isArmstrong(-153))

    def test_ispositive(self):
        self.assertTrue(ispositive(5))
        self.assertTrue(ispositive(0))
        self.assertFalse(ispositive(-1.5))

    def test_ispalindrome(self):
        self.assertTrue(ispalindrome(121))
        self.assertTrue(ispalindrome(0))
        self.assertFalse(ispalindrome(123))
        self.assertFalse(ispalindrome(-121))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)  # Legacy bug: returned 0
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_isspecial(self):
        self.assertTrue(isspecial(145))  # 1! + 4! + 5! = 1 + 24 + 120 = 145
        self.assertFalse(isspecial(100))

    def test_get_proper_divisors(self):
        self.assertEqual(get_proper_divisors(6), [1, 2, 3])
        self.assertEqual(get_proper_divisors(12), [1, 2, 3, 4, 6])
        self.assertEqual(get_proper_divisors(0), [])
        self.assertEqual(get_proper_divisors(-6), [])

    def test_isniven(self):
        self.assertTrue(isniven(18))  # 18 is div by 9
        self.assertFalse(isniven(19))
        self.assertFalse(isniven(0))

    def test_isneon(self):
        self.assertTrue(isneon(9))  # 9^2 = 81 -> 8+1=9
        self.assertFalse(isneon(8))

    def test_ismagic(self):
        self.assertTrue(ismagic(1729))  # 1+7+2+9=19 -> 1+9=10 -> 1+0=1
        self.assertTrue(ismagic(100))   # 1+0+0 = 1 (magic)
        self.assertFalse(ismagic(101))  # 1+0+1 = 2 (not magic)

    def test_isevil(self):
        self.assertTrue(isevil(9))     # bin(9) = 1001 (2 ones - even -> evil)
        self.assertTrue(isevil(10))    # bin(10) = 1010 (2 ones - even -> evil)
        self.assertFalse(isevil(11))   # bin(11) = 1011 (3 ones - odd -> not evil)
        self.assertFalse(isevil(7))    # bin(7) = 111 (3 ones - odd -> not evil)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_isdisarium(self):
        self.assertTrue(isdisarium(89))  # 8^1 + 9^2 = 89
        self.assertFalse(isdisarium(100))

    def test_isperfect(self):
        self.assertTrue(isperfect(6))  # 1+2+3 = 6
        self.assertTrue(isperfect(28))
        self.assertFalse(isperfect(12))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(-1), [])

if __name__ == "__main__":
    unittest.main()
