def ft_reduce(fn, ite):
    acc = None

    try:
        acc = next(ite)
    except StopIteration:
        raise TypeError('reduce() of an empty sequence')

    for el in ite:
        acc = fn(acc, el)
    return acc
