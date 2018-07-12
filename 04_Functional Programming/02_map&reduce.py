# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
# 比如，把这个list所有数字转为字符串：
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

###################################################################
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) 相当于 f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
     return x + y

print(reduce(add,[1,2,3,4,5]))

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def fn(x, y):
     return x * 10 + y
def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]
print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def func(x, y):
        return x * 10 + y
    def char2num_new(s):
        return DIGITS[s]
    return reduce(func, map(char2num_new, s))

# 用lambda函数进一步简化成：
def char2num_new2(s):
    return DIGITS[s]

def str2int_new(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num_new2, s))

# 练习一
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper()+name[1:].lower()
print(list(map(normalize,['adam', 'LISA', 'barT'])))

# 练习二
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def func(x,y):
        return x*y
    return reduce(func, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习三
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 思路1，将点前后的数值分开处理   ==>适用num1+num2
# 思路2，123.456=》123456/1000=123.456    ==》适用num3
def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n=s.index('.')
    # strLength=len(s)
    # n2=strLength-n
    # str1=s[:n]
    # str2=s[n+1:]
    # print(str1) #123
    # print(str2) #456
    def char2num(x):
        return digits[x]
    # num1 = reduce(lambda x, y: x*10+y, map(char2num, str1))
    # num2 = reduce(lambda x, y: x*10+y, map(char2num, str2))/pow(10, n2-1)
    num3 = reduce(lambda x, y: x*10+y, map(char2num, s.replace('.', '')))/pow(10, len(s)-n-1)
    return num3

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')