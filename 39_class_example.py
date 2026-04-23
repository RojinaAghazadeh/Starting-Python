# We want to make a class for cars.

class Car():
	"""A simple attempt to make a car."""

	def __init__(self,make,model,year):
		"""Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value, reject the change if it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def incerement(self,miles):
		"""Add the given amount to odometer reading."""
		self.odometer_reading += miles


my_new_car = Car('BMW' , 'm5' , 2016)
print(my_new_car.get_name())

my_new_car.odometer_reading = 23
my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_used_car = Car‫)‬'benz' , 'cl63' , 2018)
print(my_used_car.get_name())

my_used_car.update_odometer(15600)
my_used_car.read_odometer()
my_used_car.incerement(100)
my_used_car.read_odometer()
