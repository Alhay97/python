
ages = [40, 50 ,19]

print(ages)
print(type(ages))


list1 = [1, "hello", 3.14 , "alhai"]
print(list1)

print(list1[2])
print(list1[0])

print(list1[-2])
print(list1[-1])


list2 = ['a','l','h','a','i','i','s','i','n','42']


print(list2[2:5])
print(list2[-1:-6])
print(list2[2:])
print(list2[:])


num = [1,223,54,85,69]
print("list before: ", num)
num.append(21)
print("list after: ", num)


numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]
print(numbers)
print(even_numbers)
numbers.extend(even_numbers)

print(numbers)



numbers.insert(3,6)
numbers.insert(1,206)

print(numbers)

numbers[2] = 1997

print(numbers)


del numbers[1]

print(numbers)

del numbers[3:7]
print(numbers)


print(len(numbers))

print(1997 in numbers)

print(197 in numbers)


weird_number = [n**2 for n in range(1,11)]
print(weird_number)
