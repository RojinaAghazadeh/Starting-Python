def describe_cafe(favorite_item, cafe_name):
	"""Display information about someone's favorite item in a cafe."""
	print("\nI like " + favorite_item + ".")
	print("You can have it at " + cafe_name.title() + " cafe.")
describe_cafe('latte','host')
describe_cafe('french toast','roberto')
describe_cafe(cafe_name='cube',favorite_item='berry shake')

# When you use keyword arguments, order does not matter.
