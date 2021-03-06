# 高级特性-切片
# 取一个list或tuple的部分元素是非常常见的操作。
L = ['1', '2', '3', '4', '5']
# Python提供了切片（Slice）操作符，能大大简化这种操作。

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[0:3])
print(L[-2:])
print(L[-2:-1])
print(L[:])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
print('ABCDEFG'[::-1])  # 字符串倒序


print(list(range(100))[1::2])
