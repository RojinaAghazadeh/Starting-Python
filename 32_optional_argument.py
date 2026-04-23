def get_name(first_name='', middle_name='', last_name=''):
	"""Return a full name. """
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

name = get_name('Rojina','aghazadeh')
print(name)

name = get_name('john','lee','black')
print(name)
