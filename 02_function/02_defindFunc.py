# 空函数
# 想定义一个什么事也不做的空函数，可以用pass语句
def noneFunc():
    pass


# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError.但是如果参数类型不对，Python解释器就无法帮我们检查。
# 对参数类型做检查，只允许整数和浮点数类型的参数。
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值问题
import cmath


def move(x, y, step, angle=0):
    nx = x + step * cmath.cos(angle)
    ny = y - step * cmath.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
