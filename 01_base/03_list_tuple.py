# list是一种有序的集合，可以随时添加和删除其中的元素。
list_a = ['a', 'b', 'c']
print(list_a)
print(list_a[2])    # list的索引是从0开始，即第一个元素的index是0
print(len(list_a))  # len()函数可以获得list元素的个数
print(list_a[-1])   # -1 表示倒数第一个

# list是一个可变的有序表，所以，可以往list中追加元素到末尾，append(追加的元素)
list_a.append('d')
# 元素插入到指定的位置，比如索引号为1的位置,用insert(位置, 插入的元素)
list_a.insert(1, 'e')
print(list_a)

# 要删除list末尾的元素，用pop()方法，返回值为删除的元素，换言之，就是取出最后一个元素
print(list_a.pop())
# 删除指定位置的元素，用pop(i)方法，其中i是索引位置，换言之，就是取出索引为i的元素
print(list_a.pop(1))
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
list_a[1] = 'bb'
print(list_a)
# list里面的元素的数据类型也可以不同
list_b = ['aaa', 123, True]
print(list_b)
# list元素也可以是另一个list
list_c = ['bbbb', 'cccc']
list_b.append(list_c)
print(list_b)

print('---------tuple-----------')
# tuple,跟list的不同点为tuple不可变，
tuple1 = ('a', 'b', 'c')
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
print(tuple1[1])
print(tuple1)
# 要定义一个只有1个元素的tuple
tuple2 = (2)    # 这个是数学中的括号，当做数学运算处理
print(tuple2)
tuple3 = (2, )  # 这个才是一个元素的tuple元组
print(tuple3)

# “可变的”tuple,在tuple中加入list元素，list可变，tuple的“指向不变”
tuple4 = ('a', 'b', ['1', '2'])
print(tuple4[2][1])
print(tuple4)

# list和tuple是Python内置的有序集合，一个可变，一个不可变。
