def ft_filter(func, seq):
    if func is None:
        return [xo for xo in seq if xo]
    return [xo for xo in seq if func(xo)]


def count_in_list(lst: list, s: str):
    return len(list(ft_filter(lambda x: x == s, lst)))
