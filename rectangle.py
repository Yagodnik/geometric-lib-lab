def area(a, b): 
    '''
    Считает площадь прямоугольника

        Параметры:
            a (float): ширина прямоугольника
            b (float): высота прямоугольника

        Возвращаемое значение: 
            (float) Площадь прямоугольника размером a на b
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Считает периметр прямоугольника

        Параметры:
            a (float): ширина прямоугольника
            b (float): высота прямоугольника

        Возвращаемое значение: 
            (float) Периметр прямоугольника размером a на b
    '''
    return 2 * (a + b)


import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_perimeter(self):
        res = perimeter(2.2, 5.4)
        self.assertAlmostEqual(res, 15.2)

    def test_rectangle_area(self):
        res = area(2.2, 5.4)
        self.assertAlmostEqual(res, 11.88)