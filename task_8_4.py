def val_checker(x_func):
    def _val_checker(func):
        def wrapper(arg):
            if x_func(arg):
                result = func(arg)
                return result
            else:
                msg = f'wrong val {arg}'
                raise ValueError(msg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(5)

#calc_cube(-5)
