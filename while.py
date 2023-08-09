index = 0

while index <= 30:
	print(index)
	index+=2

#age program for voting
while True:
	name = input("enter name: ")
	if not name.strip():
		print("the name is empty, enter a valid name.")
	else:
		print("Hello {}".format(name))
		break
while True:
	age_input = input("Enter age: ")
	if not age_input.strip():
		print("Enter a number please!")
		continue
	age = int(age_input)
	if age < 0:
		print("An age cannot be a negative number")
	else:
		break

###the bellow code while craete an infinite loop becasue the condition always evaluates to True. Hence, the loop body will run for infinite times.####
while age >= 21:
	print("your  age is {} and you will be able to vote".format(age) )



#this is a simple

counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')


''''
the diference between for loop and while loop:

1- The for loop is usually used when the number of iterations is known.

2- The while loop is usually used when the number of iterations is unknown.

''''


