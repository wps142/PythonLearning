# 使用__slots__
class Student(object):
    pass
# 给实例绑定一个属性：
s=Student()
s.name="name1"
print(s.name)

# 给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2=Student()
# s2.set_age(25)  # 尝试调用方法,报错
# AttributeError: 'Student' object has no attribute 'set_age'

# 给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
     self.score =score

Student.set_score = set_score
# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
s2.set_score(90)
print(s.score)
print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 只允许对Student实例添加name和age属性。
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student2(object):
    __slots__ = ('name', 'age')

ss = Student2()
ss.age='11'
ss.name='wps'
# ss.score='20'
# AttributeError: 'Student2' object has no attribute 'score'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
     pass
g = GraduateStudent()
g.score = 9999

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。