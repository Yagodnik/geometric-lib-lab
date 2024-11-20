import math


def area(r):
    '''
    Считает площадь круга

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение: 
            (float) Площадь окружности в радиусом r
    '''

    if r < 0:
        raise ValueError("Negative circle radius")

    return math.pi * r * r


def perimeter(r):
    '''
    Считает длину окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение: 
            (float) Длина окружности радиусом r
    '''

    if r < 0:
        raise ValueError("Negative circle radius")

    return 2 * math.pi * r



import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)

    def test_area(self):
        res = area(2.2)
        self.assertAlmostEqual(res, 15.2053084434)

    def test_perimeter(self):
        res = perimeter(7.2)
        self.assertAlmostEqual(res, 45.2389342117)   

    def test_area_string(self):
        self.assertRaises(TypeError, area, "hello world")

    def test_area_negative_radius(self):
        self.assertRaises(ValueError, area, -10)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "hello world")

    def test_perimeter_negative_radius(self):
        self.assertRaises(ValueError, perimeter, -10)