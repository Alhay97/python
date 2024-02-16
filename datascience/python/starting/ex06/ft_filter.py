def ft_filter(func, seq):
    if func is None:
        return [xo for xo in seq if xo]
    return [xo for xo in seq if func(xo)]
