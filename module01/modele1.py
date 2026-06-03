# --all--,用来指定 from ...import *里面的*，eg:
# __all__=["line","add","area","PI"]


def line():
    print("-" * 30)


def add():
    print("+" * 30)

def area(r):
    a=3.14*r*r
    return a
def peri(r):
    b=3.14*r*2
    return b
PI=3.1415926
"""
1,__name__ 的值是什么？
当文件被直接运行时（比如你在终端敲 python script.py），Python 会把该文件的 __name__ 变量自动赋值为 "__main__"。
当文件被其他文件导入时（比如 import script），Python 会把该文件的 __name__ 变量赋值为该模块的名字（即文件名 "script"）
2,最经典的用法：if __name__ == '__main__'
这段代码是专门留给当前文件自己测试用的
"""
if __name__=="__main__":
    print(peri(10))



