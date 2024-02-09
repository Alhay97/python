print(type(None)) #
print(type(float("NaN")))
print(type(""))#
print(type(0))#
print(type(False))#

#submit whats bellow the comment
def NULL_not_found(object: any) -> int:
    flag = 0
    if type(object) == type(None):
        print("Nothing:", object, type(object))
    elif type(object) == int and object == 0:
        print("Zero:",object,type(object))
    elif type(object) == bool and object == False:
        print("Fake:",object,type(object))
    elif type(object) == str and object == "":
        print("Empty:",object,type(object))
    elif type(object) == float:
        print("Cheese:",object,type(object))
    else:
        flag = 1
        print("Type not Found")
    return(flag)


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found(Fake))
    
