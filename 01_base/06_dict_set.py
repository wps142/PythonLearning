# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print(d)
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
# 返回None的时候Python的交互环境不显示结果。
print(d.get('Thomas'))
print(d.get('Thomas', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# dict特点
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# list特点
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
print('-------------------------------')
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
# 重复元素在set中自动被过滤：
print(set([1, 1, 2, 2, 3, 3]))
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)    # 交集
print(s1|s2)    # 并集
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
print('------------------------------')
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = [1, 2, 3]
print(a)
a.sort()
print(a)
print('------------------------------')
# 对于不可变对象
a1 = 'abc'
print(a1.replace('a', 'A'))
print(a1)
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
