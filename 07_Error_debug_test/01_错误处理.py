# try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：

# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

# $ python3 err.py
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero

# 出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：
#
# 错误信息第1行：
#
# Traceback (most recent call last):
# 告诉我们这是错误的跟踪信息。
#
# 第2~3行：
#
#   File "err.py", line 11, in <module>
#     main()
# 调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：
#
#   File "err.py", line 9, in main
#     bar('0')
# 调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
#
#   File "err.py", line 6, in bar
#     return foo(s) * 2
# 原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
#
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# 原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
#
# ZeroDivisionError: integer division or modulo by zero
# 根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。


# 记录错误
# Python内置的logging模块可以非常容易地记录错误信息：
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。


# 最后，我们来看另一种错误处理的方式：

# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# 好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

