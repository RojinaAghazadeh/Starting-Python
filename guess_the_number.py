# We want to design a guess the number game which you can guess for five times.

import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

for guessesTaken in range(1,6):
	print("Take a guess.")
	guess = int(input())

	if guess < secretNumber:
		print("Your guess is lower.")
	elif guess > secretNumber:
		print("Your guess is too high.")
	else:
		break

if guess == secretNumber:
	print("Great job! You guessed my number in " + str(guessesTaken) + " guesses!.")
else:
	print("No. The number i was thinking of was " + str(secretNumber) + " that you couldn't guess in " + str(guessesTaken) + " guesses...")

repeat = input("Wanna play again? yes/no ")

if repeat == 'yes':
	for guessesTaken in range(1,6):
		print("Take a guess.")
		guess = int(input())

		if guess < secretNumber:
			print("Your guess is lower.")
		elif guess > secretNumber:
			print("Your guess is too high.")
		else:
			break

	if guess == secretNumber:
		print("Great job! You guessed my number in " + str(guessesTaken) + " guesses!.")
	else:
		print("No. The number i was thinking of was " + str(secretNumber) + " that you couldn't guess in " + str(guessesTaken) + " guesses...")
