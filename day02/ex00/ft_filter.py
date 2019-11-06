def ft_filter(fn, ite):
    return (el for el in ite if fn(el))
