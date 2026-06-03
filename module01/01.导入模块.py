# 导入模块
# import random
# for i in range(10):
#     print(random.randint(1,10))
# print("________________________________________________________________________")
# import random as rd  导入
# for i in range(20):
#     print(rd.randint(1,50))   调用
# 导入模块中的功能
# from random import randint as rt
# for i in range(10):
#     print(rt(1,20))

# from modele1 import area
# print(area(10))
# import modele1
# modele1.add()
# from modele1 import *   # * 和all绑定
# add()
# print(area(10))
# print(PI)
# 导入模块
# from module01 import modele1
# modele1.line()
# modele1.add()
# 导入功能
# from module01.modele1 import add,line
# add()
# line()
from module01 import *  #  #  在包里调用，要在init里面定义
modele1.add()


