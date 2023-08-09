'''
lists vs tuples:

	1-We generally use tuples for heterogeneous (different) data types and lists for
    homogeneous (similar) data types.

	2-Since tuples are immutable, iterating through a tuple is faster than with a list.
      So there is a slight performance boost.

	3-Tuples that contain immutable elements can be used as a key for a dictionary.
    With lists, this is not possible.

	4-If you have data that doesn't change, implementing it as tuple will
    guarantee that it remains write-protected.
'''



my_tuple = 1,2,3,4,5

print(my_tuple, type(my_tuple))

my_tuple2 = (1,"hello", 'a', 254.90,'a',58,'a')

print(my_tuple2)


var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

print(my_tuple2.count('a'))
print(my_tuple2.index( 254.90))

print("--------")

for i in my_tuple2:
    print(i)
