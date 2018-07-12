# 高级特性-生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
l1 = [x * x for x in range(10)]
g1 = (x * x for x in range(10))
print(l1)
print(g1)
# 可以通过next()函数获得generator的下一个返回值
# print(next(g1))
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。
for n in g1:
    print(n)

# 通过for循环来迭代它，并且不需要关心StopIteration的错误。

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b=b,a+b
        n = n + 1
    return 'end'
# 可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b=b,a+b
        n = n + 1
    return 'end'
f = fib2(6)
print(f)
print(next(f))
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 简单的例子，定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
# next(o)
# next(o)
# next(o)
# next(o)
# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。


# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

gg = fib2(6)
while True:
    try:
        x = next(gg)
        print('gg:',x)
    except StopIteration as e:
        print(e)
        break

print("---------------练习部分---------------")
#######################################################
# 杨辉三角定义如下:
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    L = [1]
    while True:
        yield L
        L = [x + y for x, y in zip([0]+L, L+[0])]



# 期待输出:
# [1]
# [1, 1] ==[0,1]+[1,0]
# [1, 2, 1]==[1,1,0]+[0,1,1]
# [1, 3, 3, 1]==[1, 2, 1, 0]+[0, 1, 2, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

# zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
print([0]+[1])
testZip = zip([1,2,3],[2,3])
for n in testZip:
    print(n)
