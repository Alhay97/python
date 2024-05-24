import numpy as np


def slice_me(famliy: list,  start: int, end: int) -> list:
    sli = np.array(famliy)
    print("old shape->", np.shape(sli))
    arr = sli[start:end,]
    print("new shape->", np.shape(arr))
    return arr


def main():
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
