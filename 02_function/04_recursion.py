# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
def fact1(n):
    if (n==1):
        return 1
    return n*fact1(n-1)

print(fact1(1))
print(fact1(3))
print(fact1(100))

# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

# 解决递归调用栈溢出的方法是通过尾递归优化，
# 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5));
# ==>fact(5)
# ==>fact_iter(5,1)
# ==>fact_iter(4,5)
# ==>fact_iter(3,5*4)
# ==>fact_iter(2,5*4*3)
# ==>fact_iter(1,5*4*3*2)
# ==>5*4*3*2=120

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
# 练习
#
# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法，
# 例如：
# -*- coding: utf-8 -*-
#汉诺塔算法
#n盘子数 a起始柱子 b辅助柱子 c终点柱子
def move(n, a, b, c):
    if n == 1:
        #只有1个盘子时,从A移动到C
        print('从',a,'移动到',c)
    else:
        #两个盘子为例时,A->B,A->C,B->C
        move(n-1 , a , c , b)#将A柱上的第一个盘子移到B柱
        move(1 , a , b , c)#将A柱剩下的一个盘子移动到C柱
        move(n-1 , b , a , c)#将B柱的剩下一个盘子移动到C柱

move(3,'A','B','C')