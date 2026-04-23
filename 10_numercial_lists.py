for value in range(1,11):
	print(value)

# Using range() to make lists
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

cubes = []
for value in range(1,21):
	cubes.append(value**3)

print(cubes)
