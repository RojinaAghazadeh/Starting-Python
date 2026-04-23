colors = ['red','blue','yellow']
print(colors)

# Accessing elements in a list
print(colors[0])

# Accessing elements in a list (capitalized)
print(colors[1].title())

# Sending messages using values from a list
message = "My first car was a " + colors[0].title() + "Honda ."
print(message)

# Changing the value of items
print(colors)
colors[0] = 'white'
print(colors)

# Adding elements to the end of a list using .append()
colors.append('black')
print(colors)

# You can also make lists using append.()
cars = []
cars.append('BMW')
cars.append('Ferrari')
cars.append('Nissan')
print(cars)

# For adding a new element at any position you can use insert()
cars.insert(2, 'Benz')
print(cars)

# Remove an item using del
del cars[0]
print(cars)

# Remove an item using pop() (it removes the last item but keeps it)
popped_cars = cars.pop()
print(cars)
print(popped_cars)

# or you can pop it from any position
first_owned = cars.pop(0)
print('The first car I owned was a ' + first_owned.title() + '.')

# when you don't know the position
cars.remove('Benz')
print(cars)
# now we have an empty list

# Sorting a list with sort()
months = ['march', 'may', 'june', 'july']
months.sort()
print(months)

#Sorting a list in reverse alphabetical order
months.sort(reverse=True)
print(months)

# If you use sorted.(), it doesn't affect the actual order of the list.

# To reverse and original list, use reverse()
