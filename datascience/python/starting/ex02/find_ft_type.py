##try for checking vatiable type
# name = 123

# ## to check if the variable is a string or not
# if type(name) == str:
#     print("is string!")
# else:
#     print("is not string")
    
# print(type(name))

# submit whats bellow under this comment
def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print(object,"is in the kitchen : <class 'str'>")
    elif type(object) == list:
        print("List : <class \'list\'>")
    elif type(object) == tuple:
        print("Tuple : <class \'tuple\'>")
    elif type(object) == set:
        print("Set : <class \'set\'>")
    elif type(object) == dict:
        print("Dict : <class \'dict\'") 
    else:
        print("Type not found")
    return(42);
    
    


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

# when the function is working is what it should print
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
