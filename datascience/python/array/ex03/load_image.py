import imageio
import numpy as np


def ft_load(path: str) -> np.array:
    data = imageio.imread(path)
    return data
