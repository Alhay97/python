import numpy as np
def slice_me(famliy: list,  start:int, end:int) ->list:
    sli = np.array(famliy)
    print("old shape->",np.shape(sli))
    arr = sli[start:end,]
    print("new shape->",np.shape(arr))
    return arr


fam = [[1.80,78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88,75.2]]


print(slice_me(fam, 0, 2))
print(slice_me(fam, 1, -2))
