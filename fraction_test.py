import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.
    # The test requires that your __eq__ is correct.
    def test__init__(self):
        self.assertIsInstance(Fraction(1, 2), Fraction)
        self.assertIsInstance(Fraction(3, 4), Fraction)
        self.assertIsInstance(Fraction(-5, 4), Fraction)
        self.assertIsInstance(Fraction(8, -9), Fraction)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(9, 12), Fraction(1, 12)+Fraction(2, 3))
        self.assertEqual(Fraction(16, 15), Fraction(2, 5)+Fraction(2, 3))
        self.assertEqual(Fraction(9, 10), Fraction(5, 10)+Fraction(2, 5))
        self.assertEqual(Fraction(26, 20), Fraction(2, 4)+Fraction(4, 5))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        a = Fraction(5, 10)
        b = Fraction(-500, -1000)
        c = Fraction(0, -1)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(b == c)

    def test_mul(self):
        self.assertEqual(Fraction(3, 8), Fraction(1, 2)*Fraction(3, 4))
        self.assertEqual(Fraction(9, 16), Fraction(-3, -4)*Fraction(-3, -4))
        self.assertEqual(Fraction(-3, 4), Fraction(-3, 2)*Fraction(1, 2))
        self.assertEqual(Fraction(3, 10), Fraction(3, 2)*Fraction(1, 5))


if __name__ == '__main__':
    unittest.main()
