## differnce between break and continue keyword

numb = [10, 20 , 30 , 40 ,100]

print("using the break keyword in for loop")
for i in numb:
	if i == 40:
		break
	print(i)


hello = [10, 20 , 30 , 40 ,100]
print("using the continue keyword in for loop")
for nb in hello:
	if nb == 30:
		continue
	print(nb)

#to print only even numbers
for db in range(101):
	if( db % 2) == 1:
		continue
	print(db)


#to print only odd numbers
for db in range(101):
	if( db % 2) == 0:
		continue
	print(db)

''''
(continue) statement with the for loop to skip the current iteration of the loop.
(break) statement is used to terminate the loop immediately when it is encountered.
''''
