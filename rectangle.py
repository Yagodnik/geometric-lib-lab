def area(a, b): 
    '''
    Считает площадь прямоугольника

        Параметры:
            a (float): ширина прямоугольника
            b (float): высота прямоугольника

        Возвращаемое значение: 
            (float) Площадь прямоугольника со сторонами a и b
    '''

    if a < 0:
        raise ValueError("Negative a side")

    if b < 0:
        raise ValueError("Negative b side")

    return a * b 

def perimeter(a, b): 
    '''
    Считает периметр прямоугольника

        Параметры:
            a (float): ширина прямоугольника
            b (float): высота прямоугольника

        Возвращаемое значение: 
            (float) Периметр прямоугольника со сторонами a и b
    '''

    if a < 0:
        raise ValueError("Negative a side")

    if b < 0:
        raise ValueError("Negative b side")

    return 2 * (a + b)


import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_area(self):
        res = area(2.2, 5.4)
        self.assertAlmostEqual(res, 11.88)

    def test_rectangle_area_string(self):
        self.assertRaises(TypeError, area, "hello world", 2)

    def test_rectangle_area_negative(self):
        self.assertRaises(ValueError, area, -10, 2)

    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "hello world", 2)

    def test_rectangle_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter, -10, 2)

    def test_rectangle_perimeter(self):
        res = perimeter(2.2, 5.4)
        self.assertAlmostEqual(res, 15.2)
