"""
Write a program (using while loop) which takes a sequence of numbers from users.
Program should stop taking input once user enter zero as input.
Program should display the sum of all the numbers entered by user.
"""

sum = 0
index = 0

while index >= 0:
    if index == 0:
    	i = int(input("enter your first number: "))
    else:
        i = int(input("enter your next number: "))
    if i == 0:
        print("the sum of all entered is: ")
        break
    sum = sum + i
    index+=1
