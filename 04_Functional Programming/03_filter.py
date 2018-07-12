# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def not_empty(s):
    return s and s.strip()

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#
# 首先，列出从2开始的所有自然数，构造一个序列：
#
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 不断筛下去，就可以得到所有的素数。

# 获取奇数生成器
def _getOddNums():
    n = 1
    while True:
        n = n + 2
        yield  n

# 除法筛选func，返回无法整除数字
def _not_divisible(n):
    return lambda x: x % n > 0

# lambda x : x+1 ===>   func(x){return x+1}

def primes():
    yield 2 # 素数第一个数是2
    it = _getOddNums()  # 生成3开始的奇数列
    while True:
        n = next(it) # 获得数列的下一个数
        yield n
        it = filter(_not_divisible(n),it) # 将数列全部拿去除以序列第一个数，筛选出的是无法整除的


# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 练习
#
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    s = str(n)
    length = len(s)    # 字符串长度
    i = 0
    while i < length / 2:
        # print(i,'+',length/2)
        if s[i] == s[length-1-i]:
            break
        else:
            return
        i = i + 1
    print('回文：', n)
    return n

def is_palindrome2(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

output2 = filter(is_palindrome2, range(1, 1000))
print('1~1000:', list(output2))
if list(filter(is_palindrome2, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')