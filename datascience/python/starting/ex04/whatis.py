# The sys module in Python provides various functions and variables 
# that are used to manipulate different parts of the Python runtime environment.
import sys

# //sys.version is used which returns a string containing the version 
# of Python Interpreter with some additional information
# print(sys.version)

# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'You entered: {line}')
# print('Exit')




# print("total number of arguments: ",n)

try:
    n = len(sys.argv)  # sys.argv is a list in Python, which contains the command-line arguments passed to the script.

    if n != 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    else:
        wo = sys.argv[1]
        try:
            i = int(wo)
            if i % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("The provided argument is not an integer")
except AssertionError as error:
    print(error)
