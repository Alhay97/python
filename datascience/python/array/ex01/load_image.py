import imageio
import numpy as np


def ft_load(path: str) -> np.array:
    data = imageio.imread(path)
    print("The shape of image is: ", np.shape(data))
    return data


def main():
    try:
        print(ft_load("./landscape.jpg"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
