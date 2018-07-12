# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 函数对象有一个__name__属性，可以拿到函数的名字：

def now():
     print('2015-3-25')
print(now.__name__)
f = now
print(f.__name__)

# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2018-6-1')

now()
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)

# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，
# 因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now():
    print('2015-3-25')

now()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

##################################################
# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
print(now.__name__)
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 针对带参数的decorator：
def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。


#
# 练习
#
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools
def metric(fn):
    # beginTime = time.time()
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        beginTime = time.time()
        f = fn(*args, **kw)
        endTime = time.time()
        print('%s executed in %s ms' % (fn.__name__, endTime-beginTime))
        return f
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')



# 小结
#
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。
#
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
#
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#
# 再思考一下能否写出一个@log的decorator，使它既支持：
def log_(text):
    # 带参数的时候，text表示第一层入参，第二层入参才是func名，需要嵌套的第二层子方法调用
    if isinstance(text,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('%s begin call' % (text))
                f = fn(*args, **kw)
                print('%s  end call' % (text))
                return f
            return wrapper
        return decorator
    else:
        # 没有带参数的时候。text表示的是func名
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call')
            f = text(*args, **kw)
            print('end call')
            return f
        return wrapper

@log_
def f111():
    pass

# 又支持：

@log_('execute')
def f222():
    pass

print(f111())
print(f222())