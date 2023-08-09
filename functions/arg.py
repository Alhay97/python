
# we use the (=) to have a defualt value for the varible

def add(a = 7, b = 10):
	print(a + b)

add(10,20)
add(a = 30)
add()

'''
the outcome:
30
40
17
'''

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

display_info('alhai', 'alhameli')


#Arbitrary Arguments: allow us to pass a varying number of values during a function call.

def find_total(*num):
	result = 0
	for numb in num:
		result += numb
	print ("total = {}".format(result))

find_total(1,33,22,55,223,54,300)

find_total(100,200,132)
