n=int(input("Enter the number to check armstrong number: "))
am = n
lgt = len(str(n))
sum1 = 0
while num != 0:
	rem = n % 10
	sum1 = sum1+(rem**lgt)
	n = n//10
if am == sum1:
	print("The given number", am, "is armstrong number")
else:
	print("The given number", am, "is not an armstrong number")
