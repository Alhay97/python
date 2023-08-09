import math

'''
examples of built-in function using the math libary:
	1-sqrt():
	2-pow():
'''

num = int(input("enter number: "))

print("square root {}".format(math.sqrt(num)))

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("{} to the power of {} is {}".format(num1, num2, pow(num1, num2)))
