import math


def area(r):
    '''
    Считает площадь круга

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение: 
            (float) Площадь окружности в радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Считает длину окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение: 
            (float) Длина окружности радиусом r
    '''
    return 2 * math.pi * r



import unittest


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(2.2)
        self.assertAlmostEqual(res, 15.2053084434)

    def test_perimeter(self):
        res = perimeter(7.2)
        self.assertAlmostEqual(res, 45.2389342117)     