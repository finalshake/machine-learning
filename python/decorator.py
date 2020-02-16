import functools

def log(func):
    @functools.wraps(func)
    def print_log(*args, **kw):
        print('begin call %s' % (func.__name__))
        func(*args, **kw)
        print('end call')
    return print_log

@log
def add(x, y):
    print(x + y)
    return x + y

res = add(200, 21)

def log_text(msg = None):
    def decor(func):
        @functools.wraps(func)
        def print_log(*args, **kw):
            print('begin call %s' % (func.__name__))
            func(*args, **kw)
            print('end call, %s' % (msg))
        return print_log
    return decor

@log_text()
def minus(x, y):
    print(x - y)
    return x - y

res = minus(10, 2)
