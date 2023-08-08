# a simple loop that runs through a list
names = ['alhai', 'ahmed', 'alhay', 'alhameli']

for i in names:
    print(i)

nm = ['saim' , 'shatha', 'bakoori', 'not me']

for n in nm:
    print("hello: {}".format(n) )



'''
the (_) symbol shoes that the element of a sequence will not be used on the loop body
''''
db = ['saim' , 'shatha', 'bakoori', 'not me']

for _ in db:
	print('Hello')
	print('Hi')


for loop with else

digits  = [0,1,5,6,7,8,10]

index = 0

for i in digits:
	index+=1
	print("number is: {} and its index: {}".format(i, index))


numb = [11,22,211,213,423]

for q in numb:
	print(q)
else:
	print("no numbers left")
