def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        for kwarg in kwargs.values():
            print(f'{func.__name__}({kwarg}: {type(kwarg)})', end=', ')
        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    return *(arg ** 3 for arg in args), *(kwarg ** 3 for kwarg in kwargs.values())


calc_cube(5, 6, x=10)
