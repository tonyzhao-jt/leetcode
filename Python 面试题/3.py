import functools
def change_param(param):
    def decorator(func):
        print(func.__name__)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(param)
            print(args)
            return func(*args, **kwargs)

        return wrapper

    return decorator  #（返回的这个在外层被调用)


def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator  #（返回的这个在外层被调用）
@change_param("para2")
@log_with_param("para1")
def test_with_param(p):
    print(test_with_param.__name__)

test_with_param('a')