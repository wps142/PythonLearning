# 高级特性-列表生成式
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
l1 = list(range(1, 11))
print(l1)
# 生成[1x1, 2x2, 3x3, ..., 10x10]
l2 = [x * x for x in range(1, 11)]
print(l2)
# 筛选出仅偶数的平方[4, 16, 36, 64, 100]
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)

# 使用两层循环，可以生成全排列
l4 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
l5 = [d for d in os.listdir('.')]
print(l5)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
l6 = [k + '=' + v for k, v in d.items()]
print(l6)

# 把一个list中所有的字符串变成小写
l7 = ['Hello', 'World', 'IBM', 'Apple']
l8 = [s.lower() for s in l7]
print(l7)
print(l8)