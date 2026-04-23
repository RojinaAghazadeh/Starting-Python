"""Gullible, by Al Sweigart al@inventwithpython.com : How to keep a gullible person busy for hours."""
print("Gullible, by Al Sweigart al@inventwithpython.com")

while True:
	print("Do you want to know how to keep a gullible person busy for hours? y/n")
	response = input('> ')
	if response.lower() == 'no' or response.lower() == 'n':
		break
	if response.lower() == 'yes' or response.lower() == 'y':
		continue
	print('"{}" is not a valid yes/no response.'.format(response))

print("Thank you. Have a nice day.")
