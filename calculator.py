#Defining functions for all operations
def add(a, b):
	return a+b
def subtract(a, b):
	return a-b
def multiply(a, b):
	return a*b
def divide(a,b):
	return a/b

#Taking user input
i = 1
while i == 1:
	try:
		num1 = float(input("Enter first number: ").strip())
		operator = input("Enter operator(+,-,*,/): ").lower().strip()
		num2 = float(input("Enter second number: ").strip())

#Performing calculations accordingly
		if operator == "+" or operator == "add" or operator == "addition":
			print(add(num1, num2))
		elif operator == "-" or operator == "subtract" or operator == "subtraction":
			print(subtract(num1, num2))
		elif operator == "*" or operator == "multiply" or operator == "multiplication":
			print(multiply(num1, num2))
		elif operator == "/" or operator == "divide" or operator == "division":
			print(divide(num1, num2))
		else:
			print("Invalid operator")
			continue

#Handling the errors
	except ValueError:
		print("Please enter valid numbers.")
		continue
	except ZeroDivisionError:
		print("Cannot divide by zero.")
		continue

#Re-running the calculator
	x = 1
	while x == 1:
		if_continue = input("Do you want to run the calculator again: y/n: ")
		if if_continue.lower().strip() == "y" or if_continue.lower().strip() == "yes":
			x = 0
		elif if_continue.lower().strip() == "n" or if_continue.lower().strip() == "no":
			x = 0
			i = 0
		else:
			print(" Enter \"y\" for yes or \"n\" for no")