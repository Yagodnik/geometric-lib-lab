
def area(a):
    '''
    Считает площадь квадрата

        Параметры:
            a (float): размер квадрата

        Возвращаемое значение: 
            (float) Площадь квадрата размером a на a
    '''

    if a < 0:
        raise ValueError("Square side is less than 0")

    return a * a


def perimeter(a):
    '''
    Считает периметр квадрата

        Параметры:
            a (float): размер квадрата

        Возвращаемое значение: 
            (float) Периметр квадрата размером a на a
    '''

    if a < 0:
        raise ValueError("Square side is less than 0")

    return 4 * a


import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_mul_string(self):
        self.assertRaises(TypeError, area, "hello world")

    def test_square_mul_negative(self):
        self.assertRaises(ValueError, area, -10)

    def test_square_perimeter(self):
        res = perimeter(2.2)
        self.assertAlmostEqual(res, 8.8)

    def test_square_area(self):
        res = area(5.4)
        self.assertAlmostEqual(res, 29.16)

    def test_square_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "hello world")

    def test_square_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter, -10)