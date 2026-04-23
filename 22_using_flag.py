# Flag acts as a signal to the program.
# So the while loop needs to check the flag.

prompt = "\nHI, What can i call you?"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
