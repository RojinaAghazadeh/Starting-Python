prompt = "\nWhat's your favorite food?"
prompt += "\nEnter 'quit' to stop the program."

while True:
	food = input(prompt)
	
	if food == 'quit':
		break
	else:
		print("Oh, i like " + food.title() + " ,too!")
