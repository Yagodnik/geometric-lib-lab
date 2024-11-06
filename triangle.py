def area(a, h): 
    '''
    Считает площадь треугольника

        Параметры:
            a (float): длина основания
            h (float): длина высоты, проведённой к основанию

        Возвращаемое значение: 
            (float) Площадь треугольника
    '''
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