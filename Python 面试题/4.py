def decrator_a(func):
    print("enter decrator_a")
    def inner_a(*args,**kwargs):
        print("enter inner_a")
        ret = func(*args,**kwargs)
        print("leaving  inner_a")
        return ret
    print("leaving decrator_a")
    return inner_a
    
	
def decrator_b(func):
    print("enter decrator_b")
    def inner_b(*args,**kwargs):
        print("enter inner_b")
        ret = func(*args,**kwargs)
        print("leaving  inner_b")
        return ret
    print("leaving decrator_b")
    return inner_b
    
	
@decrator_a
@decrator_b 
def f(*args,**kwargs):
	print("==f==")
#相当于decrator_a(decrator_b(f))
f()
