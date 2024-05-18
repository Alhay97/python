import sys

try:
    n = len(sys.argv)

    if n != 2:
        raise AssertionError("AssertionError: more than one argument provided")
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
