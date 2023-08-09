##this is a simple calcuate
import const

print("------------------------------------------------------")
print("1-> Addition			4-> Division")
print("2-> Subtraction			5-> Power of 2")
print("3-> Multiplication		6-> Power of")
print("------------------------------------------------------")

operation  = int(input("choose your operation: "))


if operation == 1:
	num1= int(input("Enter your first number: "))
	num2= int(input("Enter your second number:"))
	print(const.add(num1,num2))
elif operation == 2:
	num1= int(input("Enter your first number: "))
	num2= int(input("Enter your second number:"))
	print(const.sub(num1,num2))
elif operation == 3:
	num1= int(input("Enter your first number: "))
	num2= int(input("Enter your second number:"))
	print(const.mul(num1,num2))
elif operation == 4:
	num1= int(input("Enter your first number: "))
	num2= int(input("Enter your second number:"))
	print(const.div(num1,num2))
elif operation == 5:
	num1= int(input("Enter your first number: "))
	print(const.power2(num1))
elif operation == 6:
	num1= int(input("Enter your first number: "))
	num2= int(input("Enter your second number:"))
	print(const.powerof(num1,num2))
else:
	print("Enter a valid index of the chosen operation")
