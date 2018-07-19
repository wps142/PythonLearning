# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：
import os
print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# os.uname() # AttributeError: module 'os' has no attribute 'uname'
# 注意uname() 函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
print(os.environ.get('path'))
print(os.environ.get('x', 'default'))
# 要获取某个环境变量的值，可以调用os.environ.get('key')：


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
# 查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/', 'testdir'))

# 然后创建一个目录:
os.mkdir('testdir')

# 删掉一个目录:
os.rmdir('testdir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2


# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir/file.txt'))
# ('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/Users/michael/testdir/file.txt'))
# ('/Users/michael/testdir/file', '.txt')

# 对文件重命名:
os.rename('test.txt', 'test.py')
os.rename('test.py', 'test.txt')

# 删掉文件:
# os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
import shutil
shutil.copy('test.txt', 'test222.txt')

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print('所有目录', [x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码：
print('所有py文件', [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


print(os.path.abspath('..'))
print('上级目录', [x for x in os.listdir(os.path.abspath('..')) if os.path.isdir(x)])
