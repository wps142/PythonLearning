# type()
import types
print(type('123'))
print(type('str'))
print(type(None))
print(type(abs))

def fn():
    pass

type(fn)==types.FunctionType

type(abs)==types.BuiltinFunctionType

type(lambda x: x)==types.LambdaType

type((x for x in range(10)))==types.GeneratorType

# isinstance()
#如果继承关系是：
# object -> Animal -> Dog -> Husky
class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))         #True
print(isinstance(h, Dog))   #True
print(isinstance(d, Animal))    #True
print(isinstance(d, Dog))   #True
print(isinstance(d, Husky)) #False

# 总是优先使用isinstance()
# 判断类型，可以将指定类型及其子类“一网打尽”。


# dir()
# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(a))
print(len('asdags'))
print('asdags'.__len__())
# 比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法

# 仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(setattr(obj, 'y', 19)) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

# 也可以获得对象的方法
print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
print(fn()) # 调用fn()与调用obj.power()是一样的
# 81


# 小结
#
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

# sum = obj.x + obj.y
# 就不要写：
#
# sum = getattr(obj, 'x') + getattr(obj, 'y')

# 一个正确的用法的例子如下：

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#
# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
# 但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。