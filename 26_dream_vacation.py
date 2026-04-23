vacations = {}
active = True 

while active:
	name = input("\nHi, What's your name? ")
	vacation = input("\nIf you could visit one place in the world, where would you go? ")

	vacations[name] = vacation

	repeat = input("\nWould you like to ask your friends? yes/no ")

	if repeat == 'no':
		active = False

print("\n.....results.....")
for name, vacation in vacations.items():
	print(name + " would like to go to " + vacation.title() + ".")

