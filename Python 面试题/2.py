class fuck:

    def __init__(self, param):
        param = "shit"
    def function()
        @function_tools.wrap()


def dec_with_param(param):
    def decrator(func):
        @functools.wrap(func)
        def wrapper(*arg, **kwargs):
            return func(*arg, **kwargs)
        return wrapper
    return decrator

def dec(func, param):
    print("Decorate this func:", param)
    func()


def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator  #（返回的这个在外层被调用）
    
@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)



明确两点 一是装饰器的执行顺序从下往上,函数调用时从上往下. 二是装饰器函数在被装饰函数定义好后立即执行