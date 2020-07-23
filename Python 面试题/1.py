# print_msg 是外围函数
def print_msg():
    msg = "I'm closre"

    def printer():
        print(msg)
    return printer


# 本来变量会消失，但现在被封装在 function 里, 
# 保存了执行的上下文
closure = print_msg()
closure()

# 装饰器将函数传入装饰器函数
# functiontools.wraps(func) 把函数元信息拷贝到装饰器的 funct

def log(func):
    @functiontools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call')

# 带参数的装饰器
import functools

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



try..except..else没有捕获到异常，执行else语句

try..except..finally不管是否捕获到异常，都执行finally语句

python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。

class Singleton:
    __instance_lock = threading.lock()
    def __init__(self):
        time.sleep(1)
    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton.__instance_lock:
            if not hass
    def __new__(self, age, name):