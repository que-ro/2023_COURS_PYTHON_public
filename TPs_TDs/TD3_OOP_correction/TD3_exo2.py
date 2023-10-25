import math


class Shape:

	def calculate_area(self):
		print("Méthode de la classe de base pour calculer l'aire")


class Circle(Shape):

	def __init__(self, arg_radius):
		self.radius = arg_radius

	def calculate_area(self):
		return math.pi * self.radius ** 2


class Rectangle(Shape):

	def __init__(self, arg_width, arg_height):
		self.width = arg_width
		self.height = arg_height

	def calculate_area(self):
		return self.width * self.height


class Triangle(Shape):

	def __init__(self, arg_base, arg_height):
		self.base = arg_base
		self.height = arg_height

	def calculate_area(self):
		return (self.base * self.height) / 2


shape1 = Shape()
print(f"Area shape1:") 
shape1.calculate_area()

circle1 = Circle(3)
print(f"Area circle1: {circle1.calculate_area()}")

rectangle1 = Rectangle(2,4)
print(f"Area rectangle1: {rectangle1.calculate_area()}")

triangle1 = Triangle(3,1)
print(f"Area triangle1: {triangle1.calculate_area()}")

shapes = [circle1, rectangle1, triangle1]
for shape in shapes:
	print(shape.calculate_area())


