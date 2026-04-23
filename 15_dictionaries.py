# A dictionary in python is a collection of key-value pairs.
# A key's value can be a number, a string, a list or another dictionary.

star = {'color' : 'yellow' , 'points' : 10}
new_points = star['points']
print("YOU GOT " + str(new_points) + " POINTS!")

star['x_position'] = 0
star['y_position'] = 5
print(star)
print("\n")
# You can also start with an empty dictionary and fill it.

# In this example, we want to determine how far the star moves.

star_0 = {'x_position': 0,'y_position': 10, 'speed': 'medium'}
print("Original x-position: " + str(star_0['x_position']))

if star_0['speed'] == 'slow':
	x_increment = 1
elif star_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

print("New x-position: " + str(star_0['x_position']))

print("\n")

fav_food = {'rojina': 'kebab'}
print("Rojina's favorite food : " + fav_food['rojina'].title() + ".")

fav_food = {'sara': 'pizza','elham': 'kebab','pardis' : 'kebab','sid' : 'soup'}

for name in fav_food.keys():
	print(name.title() + "'s favorite food is " + name.title() + ".")

# You can omit key() method

# for extracting values without repeated items, use set()

print("\nThese are the following fav food: ")
for food in set(fav_food.values()):
	print(food.title())
