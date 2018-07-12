# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 位置参数
def power(x,n):
    i = 1
    while n > 0:
        n=n-1
        i=i*x
    return i

print(power(5, 5))

# 默认参数
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 当我们调用power(5)时，相当于调用power(5, 2)
# 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)
print(power2(5))
print(power2(5, 3))
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数


# 默认参数有个最大的坑
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())    # ['END']
print(add_end())    # ['END', 'END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# !!!定义默认参数要牢记一点：默认参数必须指向不变对象！!!!

def add_end_new(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end_new())
print(add_end_new())

# 可变参数
# 可变参数就是传入的参数个数是可变的
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))

# 利用可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc2(1, 2, 3))

# 如果已经有一个list或者tuple,Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums=[1, 2, 3]
print(calc2(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。
person('Michael', 30);
person('Bob', 35, city='Beijing');
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job']);
person('Jack', 24, **extra);
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。extra表示把extra这个dict的所有key

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 例如，只接收city和job作为关键字参数。
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer')
# 命名关键字参数可以有缺省值，从而简化调用：
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer');


# 参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)                        # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)                   # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')           # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)     # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)        # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)                 # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args2 = (1, 2, 3)
kw2 = {'d': 88, 'x': '#'}
f2(*args2, **kw2)               # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
