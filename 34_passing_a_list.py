def ask_who(names):
	"""Ask them who they are."""
	for name in names:
		message = "Who are you, " + name.title() + "?"
		print(message)
users = ['eli','koorosh','rojina']
ask_who(users)
