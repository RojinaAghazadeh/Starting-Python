items = ['audi','bmw','benz','nissan','honda','mclaren']

for car in items:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# This is how we check and item in a list
mycar = 'nissan'
if mycar not in items:
		print("Your car isn't a/an" + mycar.title() + ".")
else:
		print("You have a/an " + mycar.title() + ".")

age = 20
if age >= 18:
	print("\nYou are old enough to drive cause you're " + str(age) + " years old.")
else:
	print("\nYou can't drive!")

score = 89

if score < 50:
	price = 100

elif score < 80:
	price = 50
else:
	price = 0

print("\nYou should pay $" + str(price) + ".")

