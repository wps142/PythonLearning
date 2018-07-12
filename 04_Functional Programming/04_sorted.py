# 排序算法
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))     # [-21, -12, 5, 9, 36] 按从小到大排序
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21],key=abs))     # [5, 9, -12, -21, 36] 按 绝对值abs 从小到大排序排序

print(sorted(['bob', 'about', 'Zoo', 'Credit']))    # ['Credit', 'Zoo', 'about', 'bob']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # 将字符串全部转换成小写进行比较，避免大写和小写的排序问题
# ['about', 'bob', 'Credit', 'Zoo']


# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']

# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。


# 练习
#
# 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=by_score)
print(L3)