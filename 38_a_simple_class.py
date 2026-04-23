# Now we want to design a simple class.

class Human():
	"""A simple attempt to model a human."""

	def __init__(self,name,age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a human."""
		print(self.name.title() + " is now sitting. ")

human_0 = Human('henry',18)
human_0.sit()
human_1 = Human('Rojina',19)
print("And " + human_1.name.title() + " is not.")
