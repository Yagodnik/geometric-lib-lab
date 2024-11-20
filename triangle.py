def area(a, h): 
    '''
    Считает площадь треугольника

        Параметры:
            a (float): длина основания
            h (float): длина высоты, проведённой к основанию

        Возвращаемое значение: 
            (float) Площадь треугольника
    '''
    if a < 0:
        raise ValueError("Triangle a value less than 0")

    if h < 0:
        raise ValueError("Triangle h value less than 0")

    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Считает периметр треугольника

        Параметры:
            a (float): длина первой стороны
            b (float): длина второй стороны
            с (float): длина третей стороны

        Возвращаемое значение: 
            (float) Периметр треугольника треугольника
    '''
    if a < 0:
        raise ValueError("Triangle a side length less than 0")

    if b < 0:
        raise ValueError("Triangle b side length less than 0")

    if c < 0:
        raise ValueError("Triangle c side length less than 0")

    return a + b + c 


import unittest


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2.2, 3.4)
        self.assertAlmostEqual(res, 3.74)

    def test_perimeter(self):
        res = perimeter(7.2, 5.9, 1.2)
        self.assertAlmostEqual(res, 14.3)    

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, "hello world", 1)

    def test_area_negative_values_1(self):
        self.assertRaises(ValueError, area, -1, 1)

    def test_area_negative_values_2(self):
        self.assertRaises(ValueError, area, 1, -1)

    def test_area_negative_values_2(self):
        self.assertRaises(ValueError, area, -1.4, -1.1234)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, perimeter, "hello world", 1, 2)

    def test_perimeter_negative_values_1(self):
        self.assertRaises(ValueError, perimeter, -1.4, 10, 2)

    def test_perimeter_negative_values_2(self):
        self.assertRaises(ValueError, perimeter, -1.4, -10, 2)

    def test_perimeter_negative_values_3(self):
        self.assertRaises(ValueError, perimeter, -1.4, -10, -2.243423)
