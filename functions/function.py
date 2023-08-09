'''
there are two types of function:
	1- standard libary function-> built-in functions
	2- user-defined functions-> functions that were created by us based on our requirments
'''

'''
def function_name(arguments):
    # function body
    return

		1- def - keyword used to declare a function
		2- function_name - any name given to the function
		3- arguments - any value passed to function
		4- return (optional) - returns value from a function
'''

def greetings (name):
	print("hello {}".format(name))

greetings(input("enter name: "))


def addition(num1 , num2):
	sum = num1 + num2
	print('sum of {} and {} is {}'.format(num1, num2, sum))


def subtract(num1 , num2):
	subtract = num1 - num2
	print('subtraction of {} and {} is {}'.format(num1, num2, subtract))

number1 = int(input("number 1: "))
number2 = int(input("number 2: "))

addition(number1, number2)

subtract(number1, number2)


def multiplication(num1 , num2):
	total = num1 * num2
	return total


def division(num1 , num2):
	total = num1 / num2
	return total


multiplication1 = multiplication(number1, number2)
division1 = division(number1, number2)

print('multiplication of {} and {} is {}'.format(number1, number2, multiplication1))
print('division of {} and {} is {}'.format(number1, number2, division1))
