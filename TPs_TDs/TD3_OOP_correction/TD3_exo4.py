import math


class Shape:
    pass


class Circle(Shape):
    def __init__(self, arg_radius):
        self.radius = arg_radius


class Rectangle(Shape):
    def __init__(self, arg_width, arg_height):
        self.width = arg_width
        self.height = arg_height


class Triangle(Shape):

    def __init__(self, arg_base, arg_height):
        self.base = arg_base
        self.height = arg_height
		

class CalculateAreaUtility:
	
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Triangle):
            return (shape.base * shape.height) / 2
        else:
            raise TypeError("Type de forme inconnu")
		

# Testing part
circle1 = Circle(3)
rectangle1 = Rectangle(2,4)
triangle1 = Triangle(3,1)

calculate_area_utility = CalculateAreaUtility()

print(f"Aire du cercle: {calculate_area_utility.calculate_area(circle1)}")
print(f"Aire du rectangle : {calculate_area_utility.calculate_area(rectangle1)}")
print(f"Aire du triangle : {calculate_area_utility.calculate_area(triangle1)}")

