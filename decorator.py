def decorator(f):
    def wrap():

        print('haha')
        f()
        print('wuwu')
    return wrap

@decorator
def b():
    print('baba')
    return 5

b()

import time

def log_calls(func):
    def wrapper(*args,**kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__,args,kwargs))
        return_value = func(*args,**kwargs)
        print("Executed {0} in {1}ms".format(func.__name__,time.time()-now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("test1 called")

@log_calls
def test2(a,b):
    print('test2 called')

test1 = log_calls(test1)

test1(1,2,3)
test2(4,b=5)