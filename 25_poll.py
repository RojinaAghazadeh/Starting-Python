votes = {}
polling_active = True

while polling_active:
	name = input("\nEnter your name: ")
	vote = input("\nWho do you like to vote? ")

	votes[name] = vote

	repeat = input("\nIf you like to continue asking, enter 'yes' and if not, enter 'no'. ")
	if repeat == 'no':
		polling_active = False

print("\n\nResults:")
for name, vote in votes.items():
	print(name.title() + "'s" + " vote is " + vote + ".")


	
