# In this program, we start with users that need to be verified.

unconfirmed_users = ['kia','melina','sam']
confirmed_users = []

# We need to verify the unconfirmed users.

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

