number = input("Enter the number you want to know if it's odd or even: ")
number = int(number)

if number % 2 == 0:
	print("The number is even. Your number: " + str(number) )
else:
	print("The number is odd. Your number: " + str(number) )
