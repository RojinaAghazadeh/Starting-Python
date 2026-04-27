class runner():
	def __init__(self , name):
		self.name = name
	def action(self):
		print(f'{self.name} is running.')

sara = runner('Sara')

class cyclist():
	def __init__(self , name):
		self.name = name
	def action(self):
		print(f'{self.name} is cycling.')

may = cyclist('May')

for person in [sara,may]:
	print(person.action())
