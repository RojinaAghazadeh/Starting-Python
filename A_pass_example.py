# This program is designed for a person and his password.

active = True
while True:
	print("\nWho are you? ")
	name = input()
	print("\nHello, " + name.title() + ". What is your password? ")
	password = input()
	if password == 'rojina2006':
		print("\nAccess granted...")
		break
	else:
		print("\nAccess denied...")
		break
