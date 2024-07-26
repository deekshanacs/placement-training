
def add(num1, num2):
	return num1 + num2
def subtract(num1, num2):
	return num1 - num2
def multiply(num1, num2):
	return num1 * num2
def divide(num1, num2):
	return num1 / num2
print(" select an option -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


opt = int(input("Select options form 1, 2, 3, 4 :"))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if opt == 1:
	print(n1, "+", n2, "=",
					add(n1, n2))

elif opt == 2:
	print(n1, "-", n2, "=",
					subtract(n1, n2))

elif opt == 3:
	print(n1, "*", n2, "=",
					multiply(n1, n2))

elif opt == 4:
	print(n1, "/", n2, "=",
					divide(n1, n2))
else:
	print("Invalid input")
