number  = int (input("Enter a number: "))
if number > 0:
	print("{} is a positive number.".format(number))
else:
	print("{} is a negative number.".format(number))


grade  = int(input("enter grade number: "))

if grade <= 100 and grade >= 0:
	if  grade >= 50:
		if grade >= 90:
			print("A")
		elif grade < 90 and grade >= 80:
			print("B")
		elif grade < 80 and grade >= 70:
			print("C")
		elif grade < 70 and grade >= 60:
			print("D")
		print("{} is a passing grade".format(grade))
	elif grade < 60:
		print("{} is a falling grade".format(grade))
else:
	print("{} is invalid grade number".format(grade))

