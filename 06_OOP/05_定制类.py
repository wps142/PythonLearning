# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# __str__
class Student(object):
     def __init__(self, name):
         self.name = name

print(Student("jay"))
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
# 只需要定义好__str__()方法，返回一个好看的字符串就可以了：

class Student2(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return 'Student object (name: %s)' % self.name

print(Student2("jay"))

# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__=__str__

s3=Student3("jak")
print(s3)

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

# 现在，就可以按下标访问数列的任意一项了：
f=Fib2()
print(f[2])
print(f[20])
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib3(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a,b=1,1
            L= []

            for x in range(end):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

f2=Fib3()
print(f2[0:4])
# 但是没有对step参数作处理：
# >>> f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):

    def __init__(self):
        self.name = 'Michael'
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
s = Student()
print(s.name)
# print(s.score)
# AttributeError: 'Student' object has no attribute 'score'
# 错误信息很清楚地告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

class Student2(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
s2=Student2()
print(s2.score)
class Student3(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
# 调用方式要变为：
s3=Student3()
print(s3.age())

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。

# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student4(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class People(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

p=People('aaaaa')
p()     # 此时会打印出My name is aaaaa.即调用p时候会执行__call__方法

# __call__()还可以定义参数。
# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
# 因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例：

print(callable(Student()))          # False
print(callable(People('kkk')))      # True
print(callable([1, 2, 3]))          # False
print(callable(None))               # False
print(callable('str'))              # False

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
