def make_box(size,*colors):
	"""Tell the size and the color of the requested box. """
	print("\nMaking a " + str(size) + " with the following colors:")
	for color in colors:
		print("- " + color.title())
make_box(1, 'white')
make_box(2, 'white','pink')
make_box(3, 'red')
