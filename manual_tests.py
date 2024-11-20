import rectangle

print("Area(10, 5) Test")
assert(rectangle.area(10, 5) == 50)

print("Perimeter(10, 5) Test")
assert(rectangle.perimeter(10, 5) == 30)

import circle

print("Circle.Area(0) Test")
assert(circle.area(0) == 0)

print("Circle.Perimeter(0) Test")
assert(circle.perimeter(0) == 0)

import square

print("Square.Area(10, 5) Test")
assert(square.area(10) == 100)

print("Square.Perimeter(10) Test")
assert(square.perimeter(10) == 40)

import triangle

print("Triangle.Area(10, 5) Test")
assert(triangle.area(10, 5) == 25)

print("Triangle.Perimeter(10, 5, 1) Test")
assert(triangle.perimeter(10, 5, 1) == 16)

