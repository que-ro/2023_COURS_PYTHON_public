# Part 1
class Vehicle:

	def fuel_efficiency(self):
		print("Méthode de la classe de base pour calculer l'efficacité énergétique")


# Part 2
class Car(Vehicle):

	def __init__(self, arg_weight, arg_engine_power):
		self.weight = arg_weight
		self.engine_power = arg_engine_power

	def fuel_efficiency(self):
		return (self.engine_power / self.weight) * 100


class Motorcycle(Vehicle):

	def __init__(self, arg_weight):
		self.weight = arg_weight

	def fuel_efficiency(self):
		return 500 * self.weight


class Truck(Vehicle):

	def __init__(self, arg_weight, arg_cargo_weight):
		self.weight = arg_weight
		self.cargo_weight = arg_cargo_weight

	def fuel_efficiency(self):
		return 1000 / (self.weight * self.cargo_weight)


#Part 3
vehicle = Vehicle()
vehicle.fuel_efficiency()

car1 = Car(500, 200)
print(f"Fuel efficiency car1: {car1.fuel_efficiency()}")

bike1 = Motorcycle(200)
print(f"Fuel efficiency bike1: {bike1.fuel_efficiency()}")

truck1 = Truck(1000, 3000)
print(f"Fuel efficiency truck1: {truck1.fuel_efficiency()}")