# 变量可以指向函数
print(abs(-10))
print(abs)  # <built-in function abs>
f = abs
print(f)
print(f(-10))
# 这里就相当于把f指向了abs函数。调用f等于调用abs
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。


# 函数名也是变量
# abs = 10 如果拿函数名拿去指向其他值的时候
# abs(-10) 将会失效
# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
# 由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10。

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)


