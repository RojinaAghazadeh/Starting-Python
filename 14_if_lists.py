requested_toppings = ['salt','pepper','syrup']

for requested_topping in requested_toppings:
	if requested_topping == 'pepper':
		print("Sorry.")
	else:
		print(requested_topping.title() + " added.")

# if statements in multiple lists

available = ['mushrooms','olives','pine apple','sausage','extra cheese']
requested = ['mushrooms']

for requested in requested:
	if requested in available:
		print("\nokay i got your order. " + requested.title() + " added.")
	else:
		print("We are out of " + requested.title() + ".")
