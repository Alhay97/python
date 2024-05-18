import os
import math


def ft_tqdm(lst: range) -> None:
    lenght = len(list(lst))
    size = os.get_terminal_size().columns
    size -= 5
    size -= len(str(lenght)) * 2 + 3

    for i in lst:
        if i % 20 == 0:
            percent = int(i / lenght * 100)
            num_colored = math.ceil(size * percent / 100)
            num_empty = size - num_colored
            print('\r', end='')
            print(f'{percent:3}%|{"█" * num_colored}{" " * num_empty}| ', end='')
            print("{i:{lenght}}".format(i=i, lenght=len(str(lenght))), end='')
            print(f'/{lenght}', end='', flush=True)
        yield i
    print('\r', end='')
    print(f'100%|{"█" * size}{" " * 0}| ', end='')
    print("{i:{lenght}}".format(i=lenght, lenght=len(str(lenght))), end='')
    print(f'/{lenght}', end='', flush=True)
